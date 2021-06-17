import os
import webbrowser

os.system("powercfg /batteryreport /output report.html")

webbrowser.open_new_tab("report.html")