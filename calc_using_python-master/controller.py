# controller.py
from functools import partial
from convert import Converter  
ERROR_MSG = 'ERROR'

class Controller:
    """PyCalc's Controller."""
    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        self._converter = Converter()  
        # Connect signals and slots
        self._connectSignals()

    def _calculateResult(self):
        """Evaluate expressions."""
        result = self._evaluate(expression=self._view.getDisplayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()

        current_expression = self._view.getDisplayText()
        if sub_exp.startswith("bites to bytes"):
            try:
                bits = float(current_expression)
                bytes = self._converter.bitsbytes(bits)
                self._view.setDisplayText(str(bytes))
            except ValueError:
                self._view.setDisplayText(ERROR_MSG)
        elif sub_exp.startswith("bytes to bits"):
            try:
                bytes = float(current_expression)
                bits = self._converter.bytesbits(bytes)
                self._view.setDisplayText(str(bits))
            except ValueError:
                self._view.setDisplayText(ERROR_MSG)
        elif sub_exp.startswith("bytes to kilobytes"):
            
            try:
                bytes = float(current_expression)
                kilobytes = self._converter.byteskilobytes(bytes)
                self._view.setDisplayText(str(kilobytes))
            except ValueError:
                self._view.setDisplayText(ERROR_MSG)
        elif sub_exp.startswith("kilobytes to bytes"):
            
            try:
                kilobytes = float(current_expression)
                bytes = self._converter.kilobytesbytes(kilobytes)
                self._view.setDisplayText(str(bytes))
            except ValueError:
                self._view.setDisplayText(ERROR_MSG)
        elif sub_exp.startswith("bytes to megabytes"):
        
            try:
                bytes = float(current_expression)
                megabytes = self._converter.bytesmegabytes(bytes)
                self._view.setDisplayText(str(megabytes))
            except ValueError:
                self._view.setDisplayText(ERROR_MSG)
        elif sub_exp.startswith("megabytes to bytes"):
            
            try:
                megabytes = float(current_expression)
                bytes = self._converter.megabytesbytes(megabytes)
                self._view.setDisplayText(str(bytes))
            except ValueError:
                self._view.setDisplayText(ERROR_MSG)
        else:
            expression = current_expression + sub_exp
            self._view.setDisplayText(expression)

    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
