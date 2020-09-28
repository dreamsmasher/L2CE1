"""Creates a Conversions object. The convert method takes a value, \
        an optional SI prefix string to convert from, and an \
        SI suffix string to convert to."""

class Conversions:
    def __init__(self):
        prefixes = [
                "y",
                "z",
                "a",
                "f",
                "p",
                "n",
                "u",
                "m",
                "c",
                "d",
                "",
                "da",
                "h",
                "k",
                "M",
                "G",
                "T",
                "P",
                "E",
                "Z",
                "Y",
                ]
        inverse_exps = [
                24,
                21,
                18,
                15,
                12,
                9,
                6,
                3,
                2,
                1,
                0,
                -1,
                -2,
                -3,
                -6,
                -9,
                -12,
                -15,
                -18,
                -21,
                -24
                ]
        self.prefices = dict(
                            zip(
                                prefixes,
                                map(lambda x: 10 ** x, inverse_exps)
                            )
                        )

    def convert(self, val: int, base: str = "", target: str = "") -> int:
        if base not in self.prefices or target not in self.prefices:
            raise Exception("Not a valid SI unit.")
        return val * (self.prefices[target] / self.prefices[base])

    # Converts kilometers to meters
    def km_to_m(self, km):
        return self.convert(km, 'k')

    # Converts meters to kilometers
    def m_to_km(self, m):
        return self.convert(m, target='k')

    # Converts milligrams to grams
    def mg_to_g(self, mg):
      return self.convert(mg, 'm')

    # Converts milligrams to kilograms
    def mg_to_kg(self, mg):
      return self.convert(mg, 'm', 'k')

    # Converts millimeters to kilometers
    def mm_to_km(self, mm):
        return self.convert(mm, 'm', 'k')
