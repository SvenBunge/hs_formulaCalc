# coding: utf-8
import math
import time
import __builtin__ as builtins

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Hs_formulaCalc14188(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hs_formulaCalc14188")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_X0=1
        self.PIN_I_X1=2
        self.PIN_I_X2=3
        self.PIN_I_X3=4
        self.PIN_I_X4=5
        self.PIN_I_X5=6
        self.PIN_I_X6=7
        self.PIN_I_X7=8
        self.PIN_I_X8=9
        self.PIN_I_X9=10
        self.PIN_I_FORMULA_0=11
        self.PIN_I_FORMULA_1=12
        self.PIN_I_FORMULA_2=13
        self.PIN_I_CALC_ON_INIT=14
        self.PIN_O_FORMULA_OUTPUT_Y0_SBC=1
        self.PIN_O_FORMULA_OUTPUT_Y1_SBC=2
        self.PIN_O_FORMULA_OUTPUT_Y2_SBC=3
        self.PIN_O_FORMULA_OUTPUT_Y0=4
        self.PIN_O_FORMULA_OUTPUT_Y1=5
        self.PIN_O_FORMULA_OUTPUT_Y2=6
        self.PIN_O_ERROR=7
        self.PIN_O_DEBUG=8
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

        self.last_value_y0 = float('nan')
        self.last_value_y1 = float('nan')
        self.last_value_y2 = float('nan')
        self.method_dict = {}

    def on_init(self):
        time.sleep(1)  # Avoid race condition: Sometimes HS is calling on init to early before all vars are init.

        # For security reasons remove builtins-methods
        self.method_dict["__builtins__"] = {}
        # prepare call env (importlib not supported by HS 4.11, but this works well)
        self.method_dict["pow"] = getattr(math, "pow")
        self.method_dict["sqrt"] = getattr(math, "sqrt")
        self.method_dict["ceil"] = getattr(math, "ceil")
        self.method_dict["floor"] = getattr(math, "floor")
        self.method_dict["round"] = getattr(builtins, "round")
        self.method_dict["trunc"] = getattr(math, "trunc")
        self.method_dict["abs"] = getattr(builtins, "abs")
        self.method_dict["exp"] = getattr(math, "exp")
        self.method_dict["log"] = getattr(math, "log")
        self.method_dict["sin"] = getattr(math, "sin")
        self.method_dict["cos"] = getattr(math, "cos")
        self.method_dict["tan"] = getattr(math, "tan")
        self.method_dict["asin"] = getattr(math, "asin")
        self.method_dict["acos"] = getattr(math, "acos")
        self.method_dict["atan"] = getattr(math, "atan")
        self.method_dict["degrees"] = getattr(math, "degrees")
        self.method_dict["radians"] = getattr(math, "radians")
        self.method_dict["pi"] = getattr(math, "pi")
        self.method_dict["e"] = getattr(math, "e")
        self.method_dict["min"] = getattr(builtins, "min")
        self.method_dict["max"] = getattr(builtins, "max")
        self.method_dict["bool"] = getattr(builtins, "bool")
        # run the calc once after start
        if bool(self._get_input_value(self.PIN_I_CALC_ON_INIT)):
            self.calculate_formula()

    def on_input_value(self, index, value):
        self.calculate_formula()

    def calculate_formula(self):
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, formula_0, formula_1, formula_2 = self.get_inputs()
        value_dict = {"x0": x0, "x1": x1, "x2": x2, "x3": x3, "x4": x4, "x5": x5, "x6": x6, "x7": x7, "x8": x8, "x9": x9}

        try:
            if formula_0:
                value_dict.update(self.create_result_dict())
                formula_0 = self.add_security(formula_0)
                result = eval(formula_0.lower(), self.method_dict, value_dict)
                if  self._can_set_output():
                    self._set_output_value(self.PIN_O_FORMULA_OUTPUT_Y0, result)
                    if result != self.last_value_y0:  # sbc check
                        self._set_output_value(self.PIN_O_FORMULA_OUTPUT_Y0_SBC, result)
                        self.last_value_y0 = result

            if formula_1:
                value_dict.update(self.create_result_dict())  # Update y values from calculations
                formula_1 = self.add_security(formula_1)
                result = eval(formula_1.lower(), self.method_dict, value_dict)
                if self._can_set_output():
                    self._set_output_value(self.PIN_O_FORMULA_OUTPUT_Y1, result)
                    if result != self.last_value_y1:  # sbc check
                        self._set_output_value(self.PIN_O_FORMULA_OUTPUT_Y1_SBC, result)
                        self.last_value_y1 = result

            if formula_2:
                value_dict.update(self.create_result_dict())  # Update y values from calculations
                formula_2 = self.add_security(formula_2)
                result = eval(formula_2.lower(), self.method_dict, value_dict)
                if self._can_set_output():
                    self._set_output_value(self.PIN_O_FORMULA_OUTPUT_Y2, result)
                    if result != self.last_value_y2:  # sbc check
                        self._set_output_value(self.PIN_O_FORMULA_OUTPUT_Y2_SBC, result)
                        self.last_value_y2 = result

            if self._can_set_output():
                self._set_output_value(self.PIN_O_ERROR, 0)
                self._set_output_value(self.PIN_O_DEBUG, "")
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as err:
            if self._can_set_output():
                self._set_output_value(self.PIN_O_ERROR, 1)
                self._set_output_value(self.PIN_O_DEBUG, err)

    def get_inputs(self):
        x0 = self._get_input_value(self.PIN_I_X0)
        x1 = self._get_input_value(self.PIN_I_X1)
        x2 = self._get_input_value(self.PIN_I_X2)
        x3 = self._get_input_value(self.PIN_I_X3)
        x4 = self._get_input_value(self.PIN_I_X4)
        x5 = self._get_input_value(self.PIN_I_X5)
        x6 = self._get_input_value(self.PIN_I_X6)
        x7 = self._get_input_value(self.PIN_I_X7)
        x8 = self._get_input_value(self.PIN_I_X8)
        x9 = self._get_input_value(self.PIN_I_X9)
        formula_0 = self._get_input_value(self.PIN_I_FORMULA_0)
        formula_1 = self._get_input_value(self.PIN_I_FORMULA_1)
        formula_2 = self._get_input_value(self.PIN_I_FORMULA_2)
        return x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, formula_0, formula_1, formula_2

    def add_security(self, formula):
        # does not fix everything but makes me feel better
        # everyone is also kind of entitled to hack his own homeserver, isn't he?
        formula = formula.replace("import", "")
        formula = formula.replace("from", "")
        formula = formula.replace("eval", "")
        formula = formula.replace("calculate_formula", "")
        formula = formula.replace("self", "")
        formula = formula.replace("__", "")
        formula = formula.replace("{", "")
        formula = formula.replace("}", "")
        formula = formula.replace("[", "")
        formula = formula.replace("]", "")
        formula = formula.replace("\"", "")
        formula = formula.replace("'", "")
        formula = formula.replace("env", "")
        formula = formula.replace("ast", "")
        formula = formula.replace("()", "")
        formula = formula.replace("lambda", "")
        formula = formula.replace("repr", "")
        return formula

    def create_result_dict(self):
        result_dict = {}
        if not math.isnan(self.last_value_y0):
            result_dict['y0'] = self.last_value_y0
        if not math.isnan(self.last_value_y1):
            result_dict['y1'] = self.last_value_y1
        if not math.isnan(self.last_value_y2):
            result_dict['y2'] = self.last_value_y2

        return result_dict
