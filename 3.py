import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("error", ImportWarning)

warnings.warn("Warning, no code here!", SyntaxWarning)

try:
    warnings.warn("Warning, no code here!", ImportWarning)
except:
    print("Warning process")
