import tkinter


def trans():
    global entry
    global text
    text.delete('1.0', tkinter.END)
    text.insert(tkinter.END, 'https://www.baidu.com/s?wd=' + entry.get() + '&cl=3\n')
    text.insert(tkinter.END, 'https://www.google.com/search?q=' + entry.get() + '\n')
    text.insert(tkinter.END, 'https://cn.bing.com/search?q=' + entry.get() + '&qs=n\n')
    pass


tk = tkinter.Tk()
entry = tkinter.Entry(tk)
entry.pack()
button = tkinter.Button(tk, text="转化", command=trans)
button.pack()
text = tkinter.Text(tk)
text.pack()

if __name__ == '__main__':
    tk.mainloop()
