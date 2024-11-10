from ..database.database import Session
from ..database.models import Inventory as InventoryModel, Player as PlayerModel

class Inventory:
    def __init__(self, player_id, item_name, quantity=1):
        self.player_id = player_id
        self.item_name = item_name
        self.quantity = quantity

    def save(self):
        """Save or update the inventory item in the database."""
        with Session() as session:
            item = session.query(InventoryModel).filter_by(player_id=self.player_id, item_name=self.item_name).first()
            if item:
                # Update quantity if the item already exists
                item.quantity += self.quantity
            else:
                # Add new item to inventory
                item = InventoryModel(
                    player_id=self.player_id,
                    item_name=self.item_name,
                    quantity=self.quantity
                )
                session.add(item)
            session.commit()

    @classmethod
    def load(cls, player_id, item_name):
        """Load an inventory item by player_id and item_name from the database."""
        with Session() as session:
            item = session.query(InventoryModel).filter_by(player_id=player_id, item_name=item_name).first()
            if item:
                return cls(
                    player_id=item.player_id,
                    item_name=item.item_name,
                    quantity=item.quantity
                )
            else:
                print("Item not found in inventory.")
                return None

    def delete(self):
        """Delete the inventory item from the database."""
        with Session() as session:
            item = session.query(InventoryModel).filter_by(player_id=self.player_id, item_name=self.item_name).first()
            if item:
                session.delete(item)
                session.commit()
                print(f"Item '{self.item_name}' removed from the inventory.")
            else:
                print("Item not found in inventory.")
