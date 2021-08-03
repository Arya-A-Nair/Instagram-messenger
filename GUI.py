from tkinter import *
from selenium import webdriver
from time import sleep 


def new_page():
    def login():
        
        user=usern.get("1.0","end-1c")
        pswd=password.get("1.0","end-1c")
        username=receiver.get("1.0","end-1c")
        msg=message.get("1.0","end-1c")
        driver = webdriver.Chrome()
        url='https://www.instagram.com/accounts/login/'
        driver.get(url)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(pswd)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(5)
        
        driver.get('https://www.instagram.com/direct/inbox/')
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(username)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(msg)
        sleep(1)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(u'\ue007')
        driver.close()
        window.quit()
    

    global lbl,lbl2,button,usern,password
    lbl.grid_forget()
    lbl2.grid_forget()



    
    lbl=Label(right_frame,text="Who would you like to send it to",bg="skyblue")
    lbl.grid(row=0, column=1)

    receiver=Text(right_frame, height=1,width=15)
    receiver.grid(row=0, column=2)


    lbl2=Label(right_frame,text="What is the message you want to send",bg="skyblue")
    lbl2.grid(row=1, column=1)

    message=Text(right_frame,height=1,width=15)
    message.grid(row=1, column=2)

    
    button = Button(right_frame,text="Submit",command=login)
    button.grid(row=2, column=1)


window=Tk()
window.geometry("550x200")
window.maxsize(900,600)

left_frame = Frame(window, width=200, height=400, bg='skyblue')
left_frame.grid(row=0, column=0, padx=10, pady=5)
right_frame = Frame(window, width=550, height=400, bg='skyblue')
right_frame.grid(row=0, column=1, padx=10, pady=5)

window.title("Instagram message sender")
window.config(bg="skyblue")

image1=PhotoImage(file="logo.png")
original_image = image1.subsample(3,3) 
Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)


lbl=Label(right_frame,text="Enter your username",bg="skyblue")
lbl.grid(row=0, column=1)

usern=Text(right_frame, height=1,width=15)
usern.grid(row=0, column=2)


lbl2=Label(right_frame,text="Enter your password",bg="skyblue")
lbl2.grid(row=1, column=1)

password=Text(right_frame,height=1,width=15)
password.grid(row=1, column=2)


button = Button(right_frame,text="Next->",command=new_page)
button.grid(row=2, column=1)


mainloop()

