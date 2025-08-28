class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Private attribute
        self.battery_life = battery_life
        self.apps = []
    
    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed successfully!")
    
    def get_storage(self):
        return self.__storage
    
    def show_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.__storage}GB")
        print(f"Battery Life: {self.battery_life} hours")
        print(f"Installed Apps: {', '.join(self.apps) if self.apps else 'None'}")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system
    
    def activate_cooling(self):
        print(f"{self.brand} {self.model}'s {self.cooling_system} cooling activated!")
    
    def show_specs(self):  # Polymorphism
        super().show_specs()
        print(f"Cooling System: {self.cooling_system}")

# Example usage:
phone1 = Smartphone("Samsung", "Samsung A56", 128, 20)
phone1.install_app("X")
phone1.install_app("Whatsapp")
phone1.show_specs()

gaming_phone = GamingSmartphone("ASUS", "ROG Phone 7", 512, 15, "Liquid Cooling")
gaming_phone.install_app("PUBG")
gaming_phone.activate_cooling()
gaming_phone.show_specs()