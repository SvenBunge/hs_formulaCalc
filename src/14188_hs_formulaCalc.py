# coding: utf-8
import math

##!!!!##################################################################################################
#### Own written code can be placed above this commentblock . Do not change or delete commentblock! ####
########################################################################################################
##** Code created by generator - DO NOT CHANGE! **##

class Hs_formulaCalc14188(hsl20_3.BaseModule):

    def __init__(self, homeserver_context):
        hsl20_3.BaseModule.__init__(self, homeserver_context, "hs_formulaCalc14188")
        self.FRAMEWORK = self._get_framework()
        self.LOGGER = self._get_logger(hsl20_3.LOGGING_NONE,())
        self.PIN_I_FORMULA=1
        self.PIN_I_X1=2
        self.PIN_I_X2=3
        self.PIN_I_X3=4
        self.PIN_I_X4=5
        self.PIN_I_X5=6
        self.PIN_I_X6=7
        self.PIN_I_X7=8
        self.PIN_I_X8=9
        self.PIN_O_FORMULA_OUTPUT=1
        self.PIN_O_ERROR=2
        self.PIN_O_DEBUG=3
        self.FRAMEWORK._run_in_context_thread(self.on_init)

########################################################################################################
#### Own written code can be placed after this commentblock . Do not change or delete commentblock! ####
###################################################################################################!!!##

        self.last_value = -1000
        self.method_dict = {}

    def on_init(self):
        # prepare call env (importlib not supported by HS 4.11, but this works well)
        self.method_dict["sqrt"] = getattr(math, "sqrt")
        self.method_dict["pow"] = getattr(math, "pow")
        self.method_dict["ceil"] = getattr(math, "ceil")
        self.method_dict["floor"] = getattr(math, "floor")
        self.method_dict["trunc"] = getattr(math, "trunc")
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
        # run the calc once after start
        self.calculate_formula()

    def on_input_value(self, index, value):
        self.calculate_formula()  # run calc on every update

    def calculate_formula(self):
        formula, x1, x2, x3, x4, x5, x6, x7, x8 = self.get_inputs()
        formula = self.add_security(formula)
        try:
            value_dict = {"x1": x1, "x2": x2, "x3": x3, "x4": x4, "x5": x5, "x6": x6, "x7": x7, "x8": x8}
            value_dict.update(self.method_dict)  # Merge methods and vars into eval env
            result = eval(formula, value_dict)
            if result != self.last_value:  # sbc
                self._set_output_value(self.PIN_O_FORMULA_OUTPUT, result)

            self._set_output_value(self.PIN_O_ERROR, 0)
            self._set_output_value(self.PIN_O_DEBUG, "")
        except (SyntaxError, NameError, TypeError, ZeroDivisionError) as err:
            self._set_output_value(self.PIN_O_DEBUG, err)
            self._set_output_value(self.PIN_O_ERROR, 1)

    def get_inputs(self):
        formula = self._get_input_value(self.PIN_I_FORMULA)
        x1 = int(self._get_input_value(self.PIN_I_X1))
        x2 = int(self._get_input_value(self.PIN_I_X2))
        x3 = int(self._get_input_value(self.PIN_I_X3))
        x4 = int(self._get_input_value(self.PIN_I_X4))
        x5 = int(self._get_input_value(self.PIN_I_X5))
        x6 = int(self._get_input_value(self.PIN_I_X6))
        x7 = int(self._get_input_value(self.PIN_I_X7))
        x8 = int(self._get_input_value(self.PIN_I_X8))
        return formula, x1, x2, x3, x4, x5, x6, x7, x8

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
        formula = formula.replace("env", "")
        formula = formula.replace("ast", "")
        formula = formula.replace("()", "")
        formula = formula.replace("lambda", "")
        formula = formula.replace("repr", "")
        return formula
