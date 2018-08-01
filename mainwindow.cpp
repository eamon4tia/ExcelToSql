#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->importBtn, SIGNAL(clicked()), this, SLOT(onImportBtnClicked()));
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::onImportBtnClicked(){
    QString filename = QFileDialog::getOpenFileName(this,
                                                    tr("Open Excel file"),
                                                    "/home/eamon/Desktop",
                                                    "Excel file (*.xls *.xlsx)");

    std::string command = "python3 /home/eamon/github/ExcelTSql/ExcelToSQl.py -i ";
    command.append(filename.toStdString());
    command.append(" -o /home/eamon/Desktop/test.sqlite");
    system(command.c_str());
}
