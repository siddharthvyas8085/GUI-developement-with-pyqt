# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 22:54:59 2022

@author: Bisar
"""

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport


class Viewer(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(QtWidgets.QGraphicsScene(), parent)
        self.pixmap_item = self.scene().addPixmap(QtGui.QPixmap())
        self.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.setBackgroundRole(QtGui.QPalette.Dark)
        self.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.rubberBandChanged.connect(self.onRubberBandChanged)
        self.last_rect = QtCore.QPointF()

    def setPixmap(self, pixmap):
        self.pixmap_item.setPixmap(pixmap)

    def zoomIn(self):
        self.scale(1.25, 1.25)

    def zoomOut(self):
        self.scale(0.8, 0.8)

    def resetZoom(self):
        self.resetTransform()

    def fitToWindow(self):
        self.fitInView(self.pixmap_item)

    # @QtCore.pyqtSlot(QtCore.QRect, QtCore.QPointF, QtCore.QPointF)
    def onRubberBandChanged(self, rubberBandRect, fromScenePoint, toScenePoint):
        if rubberBandRect.isNull():
            pixmap = self.pixmap_item.pixmap()
            rect = self.pixmap_item.mapFromScene(self.last_rect).boundingRect().toRect()
            if not rect.intersected(pixmap.rect()).isNull():
                crop_pixmap = pixmap.copy(rect)
                label = QtWidgets.QLabel(pixmap=crop_pixmap)
                dialog = QtWidgets.QDialog(self)
                lay = QtWidgets.QVBoxLayout(dialog)
                lay.addWidget(label)
                dialog.exec_()
                # print(rect)
                # dd=str(rect).split(',')
                # ss,ss2=dd[0].split('('),dd[-1].split(')')
                # xmin,xmax,ymin,ymax=int(ss[1]),int(int(ss[1])+int(dd[2])),int(dd[1])+int(ss2[0]),int(dd[1])
                # print(xmin,xmax,ymin,ymax)
                
            self.last_rect = QtCore.QRectF()
        else:
            self.last_rect = QtCore.QRectF(fromScenePoint, toScenePoint)


class QImageViewer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.view = Viewer()
        self.setCentralWidget(self.view)

        self.printer = QtPrintSupport.QPrinter()

        self.createActions()
        self.createMenus()

        self.setWindowTitle("Image Viewer")
        self.resize(800, 600)

    def open(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "Images (*.png *.jpeg *.jpg *.bmp *.gif)",
        )
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            if pixmap.isNull():
                QtWidgets.QMessageBox.information(
                    self, "Image Viewer", "Cannot load %s." % fileName
                )
                return

            self.view.setPixmap(pixmap)

            self.printAct.setEnabled(True)
            self.fitToWindowAct.setEnabled(True)
            self.updateActions()

            if not self.fitToWindowAct.isChecked():
                pass
                # self.imageLabel.adjustSize()

    def print_(self):
        dialog = QtPrintSupport.QPrintDialog(self.printer, self)
        if dialog.exec_():
            pixmap = self.view.pixmap_item.pixmap()
            painter = QtGui.QPainter(self.printer)
            rect = painter.viewport()
            size = pixmap.size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(pixmap.rect())
            painter.drawPixmap(0, 0, pixmap)

    def fitToWindow(self):
        if self.fitToWindowAct.isChecked():
            self.view.fitToWindow()
        else:
            self.view.resetZoom()
        self.updateActions()

    def about(self):
        QtWidgets.QMessageBox.about(
            self,
            "About Image Viewer",
            "<p>The <b>Image Viewer</b> example shows how to combine "
            "QLabel and QScrollArea to display an image. QLabel is "
            "typically used for displaying text, but it can also display "
            "an image. QScrollArea provides a scrolling view around "
            "another widget. If the child widget exceeds the size of the "
            "frame, QScrollArea automatically provides scroll bars.</p>"
            "<p>The example demonstrates how QLabel's ability to scale "
            "its contents (QLabel.scaledContents), and QScrollArea's "
            "ability to automatically resize its contents "
            "(QScrollArea.widgetResizable), can be used to implement "
            "zooming and scaling features.</p>"
            "<p>In addition the example shows how to use QPainter to "
            "print an image.</p>",
        )

    def createActions(self):
        self.openAct = QtWidgets.QAction(
            "&Open...", self, shortcut="Ctrl+O", triggered=self.open
        )
        self.printAct = QtWidgets.QAction(
            "&Print...", self, shortcut="Ctrl+P", enabled=False, triggered=self.print_
        )
        self.exitAct = QtWidgets.QAction(
            "E&xit", self, shortcut="Ctrl+Q", triggered=self.close
        )
        self.zoomInAct = QtWidgets.QAction(
            "Zoom &In (25%)",
            self,
            shortcut="Ctrl++",
            enabled=False,
            triggered=self.view.zoomIn,
        )
        self.zoomOutAct = QtWidgets.QAction(
            "Zoom &Out (25%)",
            self,
            shortcut="Ctrl+-",
            enabled=False,
            triggered=self.view.zoomOut,
        )
        self.normalSizeAct = QtWidgets.QAction(
            "&Normal Size",
            self,
            shortcut="Ctrl+S",
            enabled=False,
            triggered=self.view.resetZoom,
        )
        self.fitToWindowAct = QtWidgets.QAction(
            "&Fit to Window",
            self,
            enabled=False,
            checkable=True,
            shortcut="Ctrl+F",
            triggered=self.fitToWindow,
        )
        self.aboutAct = QtWidgets.QAction("&About", self, triggered=self.about)
        self.aboutQtAct = QtWidgets.QAction(
            "About &Qt", self, triggered=QtWidgets.qApp.aboutQt
        )

    def createMenus(self):
        self.fileMenu = QtWidgets.QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.viewMenu = QtWidgets.QMenu("&View", self)
        self.viewMenu.addAction(self.zoomInAct)
        self.viewMenu.addAction(self.zoomOutAct)
        self.viewMenu.addAction(self.normalSizeAct)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fitToWindowAct)

        self.helpMenu = QtWidgets.QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.viewMenu)
        self.menuBar().addMenu(self.helpMenu)

    def updateActions(self):
        self.zoomInAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.zoomOutAct.setEnabled(not self.fitToWindowAct.isChecked())
        self.normalSizeAct.setEnabled(not self.fitToWindowAct.isChecked())


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    imageViewer = QImageViewer()
    imageViewer.show()
    sys.exit(app.exec_())