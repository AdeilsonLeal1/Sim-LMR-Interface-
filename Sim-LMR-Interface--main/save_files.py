# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_files.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from numpy import real


class Ui_Dialog_Save(object):
    def setupUi(self, Dialog, index_ref_analyte = None, ax_x = None, Reflectance_TM = None, Fwhm_TM = None, Resonance_Point_TM = None, sensibility_TM = None, fom_TM = None, simbols = None, pol = None):
        
        self.index_ref_analyte = index_ref_analyte      # List with analyte refraction indices for graph plotting
        self.Reflectance = Reflectance_TM     # List with reflectance values for plotting multiple curves in TM polarization
        self.Resonance_Point = Resonance_Point_TM  # Resonance angle or resonance wavelength  on TM polarization
        self.sensibility = sensibility_TM  # List with Sensibility values in TM polarization
        self.Fwhm = Fwhm_TM   # List with FWHM values in TM polarization
        self.ax_x = ax_x
        self.simbols = simbols
        self.polarization = pol
        self.fom = fom_TM   # Lists with the QF in TM and TE  polarizations

        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 480)
        Dialog.setWindowIcon(QtGui.QIcon('icons/LOGO.png'))
        Dialog.setWindowTitle("Save Files")
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(600, 480))
        Dialog.setMaximumSize(QtCore.QSize(700, 520))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.frame_options = QtWidgets.QFrame(Dialog)
        self.frame_options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_options.setObjectName("frame_options")
        self.formLayout = QtWidgets.QFormLayout(self.frame_options)
        self.formLayout.setObjectName("formLayout")
        self.save_default = QtWidgets.QCheckBox(self.frame_options)
        self.save_default.setChecked(True)
        self.save_default.setObjectName("save_default")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.save_default)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.save_reflectance = QtWidgets.QCheckBox(self.frame_options)
        self.save_reflectance.setChecked(True)
        self.save_reflectance.setObjectName("save_reflectance")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.save_reflectance)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.save_parameters = QtWidgets.QCheckBox(self.frame_options)
        self.save_parameters.setChecked(True)
        self.save_parameters.setObjectName("save_parameters")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.save_parameters)
        self.verticalLayout.addWidget(self.frame_options)
        self.layout_show_file = QtWidgets.QHBoxLayout()
        self.layout_show_file.setObjectName("layout_show_file")
        self.show_file_reflectance = QtWidgets.QTextBrowser(Dialog)
        self.show_file_reflectance.setObjectName("show_file_reflectance")
        self.layout_show_file.addWidget(self.show_file_reflectance)
        self.show_file_parameters = QtWidgets.QTextBrowser(Dialog)
        self.show_file_parameters.setObjectName("show_file_parameters")
        self.layout_show_file.addWidget(self.show_file_parameters)
        self.verticalLayout.addLayout(self.layout_show_file)
        self.layout_name = QtWidgets.QHBoxLayout()
        self.layout_name.setObjectName("layout_name")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.layout_name.addWidget(self.label_2)
        self.file_name = QtWidgets.QLineEdit(Dialog)
        self.file_name.setMaximumSize(QtCore.QSize(390, 16777215))
        self.file_name.setObjectName("file_name")
        self.layout_name.addWidget(self.file_name)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.layout_name.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.layout_name)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(lambda: self.save_file(Dialog)) 
        self.buttonBox.rejected.connect(Dialog.reject) 
        QtCore.QMetaObject.connectSlotsByName(Dialog)     

        self.show_text() 
    

    def show_text(self):
        self.show_file_parameters.setText(f"P-Polarization ({self.polarization})\n\n"
                                    f"Resonance {self.simbols[0]} ({self.simbols[2]}): {self.Resonance_Point}\n"
                                    f"FWHM ({self.simbols[2]}): {self.Fwhm} \n"
                                    f"Sensibility ({self.simbols[2]}/RIU): {self.sensibility}\n"
                                    f"Quality Factor: {self.fom}\n")

        self.show_file_reflectance.append(f"{self.simbols[0]},Reflectance")


    def save_file(self, Dialog):
        for i in range(len(self.index_ref_analyte)):
            file_reflectance = open(f'{self.file_name.text()}_Reflectance_vs_analyte_{str(real(self.index_ref_analyte[i])).replace(".","_")}_{self.polarization}.txt', 'w')
            file_reflectance.write(f"{self.simbols[0]},Reflectance")

            for k in range(len(self.ax_x)):
                file_reflectance.write(f"\n{self.ax_x[k]:.3f},{self.Reflectance[i][k]:.6f}")

            file_reflectance.close()
        
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Save Simulation Data")
        msg.setText("Successfully saved file")
        msg.exec()
        Dialog.close()
    


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Save Simulation Data</span></p></body></html>"))
        self.save_default.setText(_translate("Dialog", "Save all data (default)"))
        self.save_reflectance.setText(_translate("Dialog", "Reflectance vs. Analyte"))
        self.save_parameters.setText(_translate("Dialog", "Ressonance point; Sensibility; FWHM; Quality Factor;"))
        self.label_2.setText(_translate("Dialog", "Name:"))
        self.file_name.setText(_translate("Dialog", "Simulação1"))

