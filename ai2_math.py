import math

def math_eval(expr):
    expr = expr.strip().lower()
    expr = expr.replace("^", "**")
    

    allowed = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "radians": math.radians,
    }

    try:
        return eval(expr, {"__builtins__": None}, allowed)
    except:
        return "an error."
    
