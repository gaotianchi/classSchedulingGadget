import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox

from csg import Scheduler
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("排排课")
        self.setWindowIcon(QIcon("favicon.ico"))
        self.scheduler = Scheduler()
        self.input_path = ""
        self.output_path = ""
        self.filter = "Excel files (*.xls *.xlsx)"
        self.ui.toolButton.clicked.connect(self.get_input_path)
        self.ui.toolButton_2.clicked.connect(self.get_output_path)
        self.ui.lineEdit.textChanged.connect(self.update_input_path)
        self.ui.lineEdit_2.textChanged.connect(self.update_output_path)
        self.ui.pushButton.clicked.connect(self.submit)

    def get_input_path(self):
        path = QFileDialog.getOpenFileName(filter=self.filter)
        self.ui.lineEdit.setText(path[0])

    def get_output_path(self):
        path = QFileDialog.getExistingDirectory()
        self.ui.lineEdit_2.setText(path)

    def update_input_path(self):
        self.input_path = self.ui.lineEdit.text()

    def update_output_path(self):
        self.output_path = self.ui.lineEdit_2.text()

    def submit(self):
        self.scheduler.class_schedule = {}
        self.scheduler.teacher_schedule = {}
        try:
            self.scheduler.set_input_path(self.input_path)
        except:
            QMessageBox.critical(
                self, "模板-课程-职责路径异常", f"路径 {self.input_path} 异常！",
                    QMessageBox.Yes | QMessageBox.No,  # type: ignore
                    QMessageBox.Yes,  # type: ignore
            )
            return

        try:
            self.scheduler.set_output_path(self.output_path)
        except:
            QMessageBox.critical(
                self, "教师-班级-课表路径异常", f"路径 {self.output_path} 异常！",
                    QMessageBox.Yes | QMessageBox.No,  # type: ignore
                    QMessageBox.Yes,  # type: ignore
            )
            return
        
        if not self.scheduler.check_template():
            QMessageBox.critical(
                self, "处理失败", "排课失败，原因是课表模板中可分配的空位数量与课表信息中一周内的总课程数不一致！",
                    QMessageBox.Yes | QMessageBox.No,  # type: ignore
                    QMessageBox.Yes,  # type: ignore
            )
            return

        try:
            self.scheduler.process()
        except:
            QMessageBox.critical(
                self, "处理失败", "排课失败，请检查输入的数据是否符合规范。",
                    QMessageBox.Yes | QMessageBox.No,  # type: ignore
                    QMessageBox.Yes,  # type: ignore
            )
            return
        
        if self.scheduler.missing_items:
            QMessageBox.critical(
                self, "数据异常", f"排课失败，出现漏排科目({"\n".join([item[0] + "/" +  item[1] for item in self.scheduler.missing_items])})，可能的原因是上述漏排科目的优先级过低。请尝试提高上述科目的优先级，并尽量将绑定在同一教师下的科目设置为相同的优先级。\n如果还是无法解决，请联系 gaootianchi@qq.com",
                    QMessageBox.Yes | QMessageBox.No,  # type: ignore
                    QMessageBox.Yes,  # type: ignore
            )
            return
        

        self.scheduler.save_class_scheudle()
        self.scheduler.save_teacher_schedule()
        QMessageBox.information(
            self, "任务完成", f"请查看 {self.output_path} 目录下的课程表。", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes  # type: ignore
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
