import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox
import barcode
from barcode.writer import ImageWriter

class BarcodeGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Barcode Generator")
        self.setGeometry(100, 100, 400, 300)

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Input Fields
        self.invoice_label = QLabel("Numéro de facture:")
        self.invoice_input = QLineEdit()
        layout.addWidget(self.invoice_label)
        layout.addWidget(self.invoice_input)

        self.lot_label = QLabel("Lot number:")
        self.lot_input = QLineEdit()
        layout.addWidget(self.lot_label)
        layout.addWidget(self.lot_input)

        self.expiry_label = QLabel("Expiration date:")
        self.expiry_input = QLineEdit()
        layout.addWidget(self.expiry_label)
        layout.addWidget(self.expiry_input)

        self.price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        layout.addWidget(self.price_label)
        layout.addWidget(self.price_input)

        self.type_label = QLabel("Barcode Type:")
        self.type_dropdown = QComboBox()
        self.type_dropdown.addItems(["code128", "ean", "ean13"])
        layout.addWidget(self.type_label)
        layout.addWidget(self.type_dropdown)

        # Generate Button
        self.generate_button = QPushButton("Generate Barcode")
        self.generate_button.clicked.connect(self.generate_barcode)
        layout.addWidget(self.generate_button)

        # Barcode Display Area
        self.barcode_label = QLabel()
        layout.addWidget(self.barcode_label)

    def generate_barcode(self):
        invoice = self.invoice_input.text()
        lot = self.lot_input.text()
        expiry = self.expiry_input.text()
        price = self.price_input.text()
        barcode_type = self.type_dropdown.currentText()

        data = f"Invoice: {invoice}\nLot: {lot}\nExpiry: {expiry}\nPrice: {price}"
        
        # Generate barcode
        if barcode_type == "code128":
            barcode_class = barcode.Code128
        elif barcode_type == "ean":
            barcode_class = barcode.EAN13
        elif barcode_type == "ean13":
            barcode_class = barcode.EAN13
        
        generated_barcode = barcode_class(data, writer=ImageWriter())

        # Save barcode as an image
        filename = "generated_barcode"
        generated_barcode.save(filename)

        # Display barcode image
        barcode_image = QLabel()
        barcode_image.setPixmap(filename)
        self.barcode_label.setPixmap(barcode_image.pixmap())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarcodeGeneratorApp()
    window.show()
    sys.exit(app.exec_())
