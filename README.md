# PamBarGen generator
This is a simple python application made for generating significant barcode for pharmaceutical products out of its data. this project is inspired from a technical problem in a pharmacy that caused unoffecency in storing the product's informations.

## Variables details
i used the most important characteristics of a product to make its barcode which is:
- facture number: that is the day and month of the facture that the product is part of.
- lot number: the batch number of the product.
- experation date: self explanatory.
- price.

## Concern details
Out of no where, there was a constant difficulty on the stock appearing while trying to scan the product from the barcode an error message pop-up "product out of stock" wich is not the case. after analysing the problem we found out that there is a problem in generating barcodes. 
the fact of generating the barcodes as a random number is okey and kept the unicity of the barcodes for each products but even so, there where some products that have the same informations but have diffrent barcodes wich made it difficult to fuse them in the system or separate them physically. there is also some delays on the arrival of some products due to real life mistakes wich made it worse. last and not least the breakdown of the scaning equipment wich made the manual substraction of the products (after selling them) being affected without considering the barcode.