class Conversions:

  # Converts kilometers to meters
  def km_to_m(self, km):
    return km * 1_000
  
  # Converts meters to kilometers
  def m_to_km(self, m):
    solution = m / 1_000
    return solution

  # Converts milligrams to grams
  def mg_to_g(self, mg):
    solution = mg / 1_000
    return solution

  # Converts milligrams to kilograms
  def mg_to_kg(self, mg):
    solution = mg / 1_000_000
    return solution

  # Converts millimeters to kilometers
  def mm_to_km(self, mm):
    solution = mm / 1_000_000
    return solution