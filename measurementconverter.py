from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

class MeasurementConverter(object):
    def __init__(self, master):
        frame = ttk.Frame(master)
        frame.grid()
        tabControl = ttk.Notebook(root)
        tabControl.configure(width=512, height=356)

        self.weightTab = ttk.Frame(tabControl)
        tabControl.add(self.weightTab, text='Weight')
        tabControl.grid()

        self.lengthTab = ttk.Frame(tabControl)
        tabControl.add(self.lengthTab, text='Length')
        tabControl.grid()

        self.temperatureTab = ttk.Frame(tabControl)
        tabControl.add(self.temperatureTab, text='Temperature')
        tabControl.grid()

        self.display()

# Graphics

    def display(self):
        self.weightPage()
        self.lengthPage()
        self.temperaturePage()

# Light Weight Tab

    def weightPage(self):
        lightFrame = LabelFrame(self.weightTab,text='Light Convertion', height=150, width=440)
        lightFrame.grid(column=1, row=0, padx=5, pady=5)
        lightFrame.grid_propagate(0)

        gramLabel = Label(lightFrame, text='Enter Gram: ')
        gramLabel.grid(column=0, row=1, pady=3, sticky=W)
        self.gramEntry = Entry(lightFrame)
        self.gramEntry.grid(column=1, row=1, pady=3, padx=15)

        ounceLabel = Label(lightFrame, text='Enter Ounce: ')
        ounceLabel.grid(column=0, row=2, pady=3, sticky=W)
        self.ounceEntry = Entry(lightFrame)
        self.ounceEntry.grid(column=1, row=2, pady=3, padx=15)

        lightLabel = Label(lightFrame, text='Result: ')
        lightLabel.grid(column=0, row=3, pady=5, sticky=W)
        self.lightField = Label(lightFrame, text='')
        self.lightField.grid(column=1, row=3, pady=5)

        submitButton = Button(lightFrame, text='Submit', command=self.lightConverter)
        submitButton.grid(column=2, row=1, rowspan=2, padx=5, pady=5, sticky=E)

# Heavy Weight Tab

        heavyFrame = ttk.LabelFrame(self.weightTab,text='Heavy Convertion', height=150, width=440)
        heavyFrame.grid(column=1, row=5, padx=5, pady=5)
        heavyFrame.grid_propagate(0)

        kiloLabel = Label(heavyFrame, text='Enter Kilo: ')
        kiloLabel.grid(column=0, row=6, pady=3, sticky=W)
        self.kiloEntry = Entry(heavyFrame)
        self.kiloEntry.grid(column=1, row=6, pady=3, padx=15)

        poundLabel = Label(heavyFrame, text='Enter Pound: ')
        poundLabel.grid(column=0, row=7, pady=3, sticky=W)
        self.poundEntry = Entry(heavyFrame)
        self.poundEntry.grid(column=1, row=7, pady=3, padx=15)

        heavyLabel = Label(heavyFrame, text='Result: ')
        heavyLabel.grid(column=0, row=8, pady=5, sticky=W)
        self.heavyField = Label(heavyFrame, text='')
        self.heavyField.grid(column=1, row=8, pady=5)

        submitButton = Button(heavyFrame, text='Submit', command=self.heavyConverter)
        submitButton.grid(column=2, row=6, rowspan=2, padx=5, pady=5, sticky=E)

# Short Length Tab

    def lengthPage(self):
        shortFrame = LabelFrame(self.lengthTab,text='Short Convertion', height=150, width=440)
        shortFrame.grid(column=1, row=0, padx=5, pady=5)
        shortFrame.grid_propagate(0)

        cmLabel = Label(shortFrame, text='Enter Centimetre: ')
        cmLabel.grid(column=0, row=1, pady=3, sticky=W)
        self.cmEntry = Entry(shortFrame)
        self.cmEntry.grid(column=1, row=1, pady=3, padx=15)

        inchLabel = Label(shortFrame, text='Enter Inch: ')
        inchLabel.grid(column=0, row=2, pady=3, sticky=W)
        self.inchEntry = Entry(shortFrame)
        self.inchEntry.grid(column=1, row=2, pady=3, padx=15)

        shortLabel = Label(shortFrame, text='Result: ')
        shortLabel.grid(column=0, row=3, pady=5, sticky=W)
        self.shortField = Label(shortFrame, text='')
        self.shortField.grid(column=1, row=3, pady=5)

        submitButton = Button(shortFrame, text='Submit', command=self.shortConverter)
        submitButton.grid(column=2, row=1, rowspan=2, padx=5, pady=5, sticky=E)

# Long Length Tab

        longFrame = LabelFrame(self.lengthTab,text='Long Convertion', height=150, width=440)
        longFrame.grid(column=1, row=4, padx=5, pady=5)
        longFrame.grid_propagate(0)

        kmLabel = Label(longFrame, text='Enter Kilometre: ')
        kmLabel.grid(column=0, row=5, pady=3, sticky=W)
        self.kmEntry = Entry(longFrame)
        self.kmEntry.grid(column=1, row=5, pady=3, padx=15)

        mileLabel = Label(longFrame, text='Enter Mile: ')
        mileLabel.grid(column=0, row=6, pady=3, sticky=W)
        self.mileEntry = Entry(longFrame)
        self.mileEntry.grid(column=1, row=6, pady=3, padx=15)

        longLabel = Label(longFrame, text='Result: ')
        longLabel.grid(column=0, row=7, pady=5, sticky=W)
        self.longField = Label(longFrame, text='')
        self.longField.grid(column=1, row=7, pady=5)

        submitButton = Button(longFrame, text='Submit', command=self.longConverter)
        submitButton.grid(column=2, row=5, rowspan=2, padx=5, pady=5, sticky=E)

# Temperature Tab

    def temperaturePage(self):
        temperatureFrame = LabelFrame(self.temperatureTab,text='Temperature Convertion', height=200, width=440)
        temperatureFrame.grid(column=1, row=0, padx=5, pady=5)
        temperatureFrame.grid_propagate(0)

        celsiusLabel = Label(temperatureFrame, text='Enter Celsius: ')
        celsiusLabel.grid(column=0, row=1, pady=3, sticky=W)
        self.celsiusEntry = Entry(temperatureFrame)
        self.celsiusEntry.grid(column=1, row=1, pady=3, padx=15)

        fahrenheitLabel = Label(temperatureFrame, text='Enter Fahrenheit: ')
        fahrenheitLabel.grid(column=0, row=2, pady=3, sticky=W)
        self.fahrenheitEntry = Entry(temperatureFrame)
        self.fahrenheitEntry.grid(column=1, row=2, pady=3, padx=15)

        temperatureLabel = Label(temperatureFrame, text='Result: ')
        temperatureLabel.grid(column=0, row=4, pady=5, sticky=W)
        self.temperatureField = Label(temperatureFrame, text='')
        self.temperatureField.grid(column=1, row=4, pady=5)

        submitButton = Button(temperatureFrame, text='Submit', command=self.temperatureConverter)
        submitButton.grid(column=2, row=1, rowspan=2, padx=5, pady=5, sticky=E)


# Weight Functions

    def lightConverter(self):
        try:
            gram = self.gramEntry.get()
            if self.gramEntry.get() == '':
                gram = 0
            else:
                gram = float(gram)
            ounce = self.ounceEntry.get()
            if self.ounceEntry.get() == '':
                ounce = 0
            else:
                ounce = float(ounce)
            gramRes = round(ounce * 28.34925, 2)
            ounceRes = round(gram / 28.34952, 2)
            sum = str(f'''
            {ounceRes} oz.
            {gramRes} g.
            ''')
            self.lightField.configure(text=sum)
        except ValueError:
            self.lightField.configure(text='Invalid Data!')

    def heavyConverter(self):
        try:
            kilo = self.kiloEntry.get()
            if self.kiloEntry.get() == '':
                kilo = 0
            else:
                kilo = float(kilo)
            pound = self.poundEntry.get()
            if self.poundEntry.get() == '':
                pound = 0
            else:
                pound = float(pound)
            kiloRes = round(pound / 2.20462262, 2)
            poundRes = round(kilo * 2.20462262, 2)
            sum = str(f'''
            {poundRes} lbs.
            {kiloRes} kg.
            ''')
            self.heavyField.configure(text=sum)
        except ValueError:
            self.heavyField.configure(text='Invalid Data!')

# Length Functions

    def shortConverter(self):
        try:
            cm = self.cmEntry.get()
            if self.cmEntry.get() == '':
                cm = 0
            else:
                cm = float(cm)
            inch = self.inchEntry.get()
            if self.inchEntry.get() == '':
                inch = 0
            else:
                inch = float(inch)
            cmRes = round(inch * 2.54, 2)
            inchRes = round(cm / 2.54, 2)
            sum = str(f'''
            {inchRes} inch.
            {cmRes} cm.
            ''')
            self.shortField.configure(text=sum)
        except ValueError:
            self.shortField.configure(text='Invalid Data!')

    def longConverter(self):
        try:
            km = self.kmEntry.get()
            if self.kmEntry.get() == '':
                km = 0
            else:
                km = float(km)
            mile = self.mileEntry.get()
            if self.mileEntry.get() == '':
                mile = 0
            else:
                mile = float(mile)
            kmRes = round(mile * 1.609344, 2)
            mileRes = round(km / 1.609344, 2)
            sum = str(f'''
            {mileRes} mile.
            {kmRes} km.
            ''')
            self.longField.configure(text=sum)
        except ValueError:
            self.longField.configure(text='Invalid Data!')

# Temperature Functions

    def temperatureConverter(self):
        try:
            celsius = self.celsiusEntry.get()
            if self.celsiusEntry.get() == '':
                celsius = 0
            else:
                celsius = float(celsius)
            fahrenheit = self.fahrenheitEntry.get()
            if self.fahrenheitEntry.get() == '':
                fahrenheit = 0
            else:
                fahrenheit = float(fahrenheit)
            celsiusRes = round((fahrenheit - 32) / 1.8, 2)
            fahrenheitRes = round(celsius * 9 / 5 + 32, 2)
            sum = str(f'''
            {fahrenheitRes} ℉.
            {celsiusRes} °C.
            ''')
            self.temperatureField.configure(text=sum)
        except ValueError:
            self.temperatureField.configure(text='Invalid Data!')


if __name__ == '__main__':
    root = Tk()
    root.title('Measurement Converter')
    root.geometry('515x360')
    root.configure(bg='gray25')
    main = MeasurementConverter(root)
    root.mainloop()
