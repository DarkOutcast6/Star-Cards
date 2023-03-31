# Main.py
class Card:
	def __init__(self, name, rarity, category, brand, shiny=False, signed=False, chromed=False):
		self.name = name
		self.rarity = rarity
		self.category = category
		self.brand = brand
		self.shiny = shiny
		self.signed = signed
		self.chromed = chromed


hello = "meow"
HTML=f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Download</title>
</head>
<body>
	<h2>{hellow}</h2>
</body>
</html>
"""
with open("test.html","w") as f:
    f.write(HTML)
