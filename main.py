import dearpygui.dearpygui as dpg
import os.path as path
import sys
from math import *

dpg.create_context()
dpg.setup_dearpygui()
dpg.create_viewport(width=800, height=520)
with dpg.font_registry():
    try:
        base=sys._MEIPASS
        print(base)
        font_path = path.join(base, "font.ttf")
        font_path2 = path.join(base, "bold.ttf")
    except:
        font_path = "font.ttf"
        font_path2 = "bold.ttf"
    font = dpg.add_font(font_path, 18)
    large_font = dpg.add_font(font_path2, 40)
    dpg.bind_font(font)

with dpg.window(tag="main window"):
    title = dpg.add_text("HYPER CALCULAR")
    dpg.bind_item_font(title, large_font)
    x_series = [x for x in range(-1000, 1000)]
    y_series = [y for y in x_series]
    y_series2 = [y for y in x_series]
    with dpg.group(horizontal=True):
        with dpg.plot(width=400, height=400, label="Plot", tag="plot") as plot:
            dpg.add_plot_axis(dpg.mvXAxis, label="X", tag="X")
            dpg.add_plot_axis(dpg.mvYAxis, label="Y", tag="Y")
            dpg.add_line_series(x_series,
                                y_series,
                                tag="line",
                                parent="Y")

            dpg.add_line_series(x_series,
                                y_series2,
                                tag="line2",
                                parent="Y")

        with dpg.group(horizontal=False):
            def update_lines(x, y):
                global y_series, y_series2
                f1 = dpg.get_value("f1")
                f2 = dpg.get_value("f2")
                eqM = dpg.get_value("eqM")
                y_series = []
                for x in x_series:
                    try:
                        a = eval(dpg.get_value("a"))
                        b = eval(dpg.get_value("b"))
                        c = eval(dpg.get_value("c"))
                        d = eval(dpg.get_value("d"))
                        res = eval(f1,)
                        y_series.append(res)
                    except:
                        y_series.append(0)
                y_series2 = []
                for x in x_series:
                    try:
                        a = eval(dpg.get_value("a"))
                        b = eval(dpg.get_value("b"))
                        c = eval(dpg.get_value("c"))
                        d = eval(dpg.get_value("d"))
                        res = eval(f2,)
                        y_series2.append(res)
                    except:
                        y_series2.append(0)
                dpg.set_value("line", (x_series, y_series))
                dpg.set_value("line2", (x_series, y_series2))
                if eqM:
                    result = -1
                    print(x_series)
                    for pick, index in enumerate(x_series):
                        if y_series[index] == y_series2[index]:
                            if pick==0:
                                return
                            result = x_series[index]
                            print(x_series[index])
                            print(y_series[index] == y_series2[index])
                            print(y_series[index], " ",y_series2[index])
                            break
                    dpg.set_value("res", result)
                    with dpg.window() as modal:
                        txt = dpg.add_text(str(result))
                        dpg.bind_item_font(txt, large_font)
                        dpg.add_button(label="close", callback=lambda x, y: dpg.delete_item(modal))


            dpg.add_input_text(label="formula 1", tag="f1", width=250, default_value="x")
            dpg.add_input_text(label="formula 2", tag="f2", width=250, default_value="x")
            dpg.add_checkbox(label="equation mode", tag="eqM", default_value=True)
            dpg.add_button(label="calculate the calculation", callback=update_lines)
            dpg.add_text("custom variables/expressions")
            dpg.add_input_text(label="a", tag="a", width=250, default_value="0")
            dpg.add_input_text(label="b", tag="b", width=250, default_value="0")
            dpg.add_input_text(label="c", tag="c", width=250, default_value="0")
            dpg.add_input_text(label="d", tag="d", width=250, default_value="0")
            dpg.add_text("result here if equation mode", tag="res")
dpg.set_primary_window("main window", True)
dpg.set_viewport_always_top(True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
