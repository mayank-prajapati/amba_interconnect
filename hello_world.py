import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def _init_(self):
        Gtk.Window._init_(self, title="Hello World")
        self.button = Gtk.Button(lable="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
	
    def on_button_clicked(self, widget):
        print ("Hello World")


win = MyWindow()
#win.on_button_clicked("");
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()