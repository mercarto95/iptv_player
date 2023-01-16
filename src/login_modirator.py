import _parser_, os, login_menu, main_menu, Tv, Account
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import _parser_
import vlc
import os 
import main_menu_modirator


comBox_is_readed = False 

def login_existing_account_clicked(obj):
    global comBox_is_readed
    print("show existing accounts menu")
    obj.txtBox_username.setText("")
    obj.txtBox_name.setText("")
    obj.txtBox_password.setText("")
    obj.txtBox_server.setText("")
    obj.widget_1.setCurrentIndex(1)
    if comBox_is_readed:
        return
    obj.account = Account.Account()  # account = list of lines, each line = "name, username, password, server"
    lines = obj.account.read_accounts_from_database()
    if lines is not None and lines is not False and len(lines) > 0:
        for line in lines:
            x = line.split(", ")
            obj.comboBox_existing_account.addItem(x[0])
    comBox_is_readed = True

def login_new_account_menu_clicked(obj):
    print("show new accounts menu")
    obj.txtBox_username.setText("")
    obj.txtBox_name.setText("")
    obj.txtBox_password.setText("")
    obj.txtBox_server.setText("")
    obj.widget_1.setCurrentIndex(0)

def login_submit_new_account_clicked(obj):
    obj.btn_enter_existing.setEnabled(False)
    obj.btn_submit_exist.setEnabled(False)
    obj.btn_existing_account.setEnabled(False)
    obj.btn_new_account.setEnabled(False)
    print("submit new account")
    name = obj.txtBox_name.text()
    username = obj.txtBox_username.text()
    password = obj.txtBox_password.text()
    server_link = obj.txtBox_server.text()
    if name == "" or username == "" or password == "":
        obj.show_msg("Fill all fields, please!")
        return
    
    account =  Account.Account(name, username, password, server_link)
    if account == None:
        print("Can not create account instance. ")
        obj.show_msg("Error, can not create this account")
        ##   
    import request_service
    x = request_service.request_data(account)  
    obj.tv = Tv.Tv( x, new_tv=True)
    obj.btn_enter_existing.setEnabled(True)
    obj.btn_submit_exist.setEnabled(True)
    obj.btn_existing_account.setEnabled(True)
    obj.btn_new_account.setEnabled(True)
    if x == False:                                         ## display msg box error 
        obj.show_msg("Faild to request the service. Please check your login information")
    elif x == None:
        obj.show_msg("Faild to store data in cache. Try again or report us the problem ( inc. your login info ) to fix the bugg asap.")
    #### Need to read the channels file of the choosen tv . name of the file = (tv_name + extention)
    else:
        obj.btn_enter_existing.setEnabled(True)
        obj.btn_submit_exist.setEnabled(True)
        obj.btn_existing_account.setEnabled(True)
        obj.btn_new_account.setEnabled(True)
        if obj.tv.is_loaded == False:
            obj.show_msg("Error while parsing the new tv (line 65)")
            return
        obj.login_successed = True
        print(f"login  =  {obj.login_successed}")
        obj.app.exit()
        print("Will this be exexuted???")

    obj.frame_2.hide()

def login_submit_existing_account_clicked(obj):
    print("submit existing account ")
    tv_name = obj.comboBox_existing_account.currentText()
    x = obj.account.confirm_existing_account(tv_name)
    if x == False:
        obj.show_msg("Can not confirm the choosen tv")
        return False
    #### Need to read the channels file of the choosen tv . name of the file = (tv_name + extention)
    path = "./data/"   ######################################################## Make it dynamic
    tv_name = path +  tv_name + ".bi"
    obj.tv = Tv.Tv(tv_name)
    if obj.tv.is_loaded == False:
        obj.frame_2.hide()
        obj.show_msg("Error, Can not find the cached file, try to update tv / request new")
        obj.btn_enter_existing.setEnabled(True)
        obj.btn_submit_exist.setEnabled(True)
        obj.btn_existing_account.setEnabled(True)
        obj.btn_new_account.setEnabled(True)
        return
    obj.frame_2.hide()
    obj.login_successed = True
    print(f"login  =  {obj.login_successed}")
    obj.app.exit()
    print("Will this be exexuted???")


def login_show_waiting_menu(obj):
    read_from_cache = obj.radioButton_read_from_file.isChecked()
    make_new_request = obj.radioButton_update_file.isChecked()
    if read_from_cache == make_new_request == False:
        obj.show_msg("Choose: read from cache OR update file, Please! ")
        return
    obj.btn_new_account.setEnabled(False)
    obj.btn_existing_account.setEnabled(False)
    obj.btn_enter_existing.setEnabled(False)
    print("Going to waiting_frame now now")
    obj.frame_2.show()







