class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return f"{self.artist}. \"{self.title}\". {self.year}, {self.medium}. {self.owner.name}, {self.owner.location}."

class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    return self.listings

  def remove_listing(self, listing):
    self.listings.remove(listing)
    return self.listings

  def show_listings(self):
    print("\n Listings: \n")
    for listing in self.listings:
      print(listing)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    if artwork.owner.name == self.name:
      listing = Listing(artwork, price, self)
      veneer.add_listing(listing)
    else:
      return f"{artwork.owner} doesn't own that piece."

  def buy_artwork(self, artwork):
    if (artwork.owner.name != self.name):
      for listing in veneer.listings:
        if listing.art.title == artwork.title:
          art_listing = listing
          artwork.owner = self
          veneer.remove_listing(art_listing)


class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return f"{self.art.title}, {self.price}"
  

edytta = Client('Edytta Halpirt', "Private Collection", False)
moma = Client('The MOMA', "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
print(girl_with_mandolin)

veneer = Marketplace()
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
print(veneer.show_listings())
moma.buy_artwork(girl_with_mandolin)
print(veneer.show_listings())
print(girl_with_mandolin)
