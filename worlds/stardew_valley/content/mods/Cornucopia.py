from ..game_content import ContentPack, StardewContent
from ..mod_registry import register_mod_content_pack
from ..override import override
from ...data.harvest import ForagingSource, SeasonalForagingSource, FruitBatsSource, MushroomCaveSource, HarvestFruitTreeSource, HarvestCropSource
from ...data.requirement import YearRequirement, SeasonRequirement
from ...mods.mod_data import ModNames
from ...strings.crop_names import CornFruit, CornVegetable, CornCropExtFruit, CornCropExtVegetable, CornHerbExtVegetable, CornTreeExtFruit, Fruit
from ...strings.flower_names import CornFlower, CornCropExtFlower
from ...strings.forageable_names import CornForageable, CornCropExtForageable, CornTreeExtForageable, CornHerbExtForageable, Forageable
from ...strings.fruit_tree_names import CornSapling, CornCropExtSapling, CornHerbExtSapling, CornTreeExtSapling
from ...strings.season_names import Season
from ...strings.region_names import Region
from ..vanilla.ginger_island import ginger_island_content_pack as ginger_island_content_pack
from ...strings.seed_names import CornSeed, CornCropExtSeed, CornHerbExtSeed
from ...data.game_item import ItemTag, ItemSource, Tag
from ...data.shop import ShopSource
from ...strings.generic_names import Generic
from ...strings.material_names import Material
from ...strings.region_names import Region, LogicRegion
from ...strings.currency_names import Currency
from ...strings.fish_names import Fish, WaterItem
from ...string.metal_names import Fossil
#from ...data import flower_names, crop_names, seed_names, fruit_tree_names, forageable_names








class CornContentPack(ContentPack):
    def crop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.harvest_sources.pop(CornFlower.vanilla.name)
            content.harvest_sources.pop(CornVegetable.peppercorn.name)
            
    def shop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.shop_sources.pop(CornSapling.vanilla.name)
            content.shop_sources.pop(CornSapling.peppercorn.name)
            
class CornCropExtContentPack(ContentPack):
    def crop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.harvest_sources.pop(CornCropExtFruit.passion_fruit.name)
            
    def shop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.shop_sources.pop(CornCropExtSeed.passion_fruit.name)

class CornTreeExtContentPack(ContentPack):
    def crop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.harvest_sources.pop(CornTreeExtFruit.durian.name)
            content.harvest_sources.pop(CornTreeExtFruit.papaya.name)
            content.harvest_sources.pop(CornTreeExtFruit.plantain.name)
            
    def shop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.shop_sources.pop(CornTreeExtSapling.durian.name)
            content.shop_sources.pop(CornTreeExtSapling.papaya.name)
            content.shop_sources.pop(CornTreeExtSapling.plantain.name)
  




register_mod_content_pack(CornContentPack(
    ModNames.cornucopia,
   
    harvest_sources={
        CornVegetable.basil: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.basil, seasons=(Season.spring,)),),
        CornVegetable.cucumber: (Tag(ItemTag.Vegetable), HarvestCropSource(seed=CornSeed.cucumber, seasons=(Season.summer,)),),
        CornVegetable.lettuce: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.lettuce, seasons=(Season.summer,)),),
        CornVegetable.onion: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.onion, seasons=(Season.spring,)),),
        CornVegetable.peanut: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.peanut, seasons=(Season.fall,)),),
        CornVegetable.spinach: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.spinach, seasons=(Season.spring, Season.fall)),),
        CornVegetable.sugarcane: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.sugarcane, seasons=(Season.summer,)),),
        CornVegetable.turnip: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.turnip, seasons=(Season.fall,)),),
        CornVegetable.zucchini: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSeed.zucchini, seasons=(Season.fall,)),),
        CornVegetable.olive: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSapling.olive, seasons=(Season.fall,)),),
        CornFruit.bell_pepper: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornSeed.bell_pepper, seasons=(Season.summer,)),),
        CornFruit.kiwi: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornSeed.kiwi, seasons=(Season.summer,)),),
        CornFruit.watermelon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornSeed.watermelon, seasons=(Season.summer,)),),
        CornFruit.avocado: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornSapling.avocado, seasons=(Season.summer,)),),
        CornFruit.pear: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornSapling.pear, seasons=(Season.winter,)),),
        CornFruit.raspberry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornSapling.raspberry, seasons=(Season.summer,)), ForagingSource(regions=(Region.forest, Region.mountain, Region.town), season=(Season.summer,))),
        CornFruit.cotton: (HarvestCropSource(seed=CornSeed.cotton, seasons=(Season.summer, Season.fall)),),
        CornFruit.cocoa: (HarvestCropSource(seed=CornSapling.cocoa, seasons=(Season.spring,)),),
        CornFruit.pistachio: (HarvestCropSource(seed=CornSapling.pistachio, seasons=(Season.fall,)),),
        CornFruit.soybean: (Tag(ItemTag.SEED), HarvestCropSource(seed=CornSeed.soybean_starter, seasons=(Season.fall,)),),
        CornFlower.vanilla: (Tag(ItemTag.FLOWER), HarvestCropSource(seed=CornSeed.vanilla, seasons=(Season.spring,)),),
        CornVegetable.peppercorn: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornSapling.peppercorn, seasons=(Season.spring, Season.summer, Season.fall)), ForagingSource(regions=(Region.forest, Region.mountain), seasons=(Season.spring,),), ForagingSource(regions=(Region.island_east, Region.island_west, Region.island_south))),
         
        
        },
    shop_sources={
        CornSeed.cotton: (ShopSource(money_price=200, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall)), ShopSource(items_price=((250, Currency.star_token),), shop_region=LogicRegion.fair),),
        CornSapling.cocoa: (ShopSource(money_price=5000, shop_region=Region.pierre_store),),
        CornSapling.pistachio: (ShopSource(money_price=3750, shop_region=Region.pierre_store),),
        CornSeed.soybean_starter: (ShopSource(money_price=2000, shop_region=Region.traveling_cart, seasons=(Season.fall,),),),
        CornSeed.bell_pepper: (ShopSource(money_price=130, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornSeed.basil: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornSeed.turnip: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornSeed.cucumber: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornSeed.kiwi: (ShopSource(money_price=100, shop_region=LogicRegion.luau), ShopSource(items_price=((1, Fish.tuna),), shop_region=Region.island_trader),),
        CornSeed.lettuce: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornSeed.onion: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornSeed.peanut: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornSeed.spinach: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.spring, Season.fall)),),
        CornSeed.sugarcane: (ShopSource(money_price=20, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornSeed.watermelon: (ShopSource(money_price=300, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)), ShopSource(money_price=300, shop_region=LogicRegion.luau),),
        CornSeed.zucchini: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornSapling.olive: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornSapling.raspberry: (ShopSource(money_price=500, shop_region=Region.pierre_store),),
        CornSapling.avocado: (ShopSource(money_price=8000, shop_region=Region.pierre_store),),
        CornSapling.pear: (ShopSource(money_price=5500, shop_region=Region.pierre_store),),
        CornSapling.vanilla: (ShopSource(items_price=((1, Forageable.rainbow_shell),), shop_region=Region.island_trader),),
        CornSapling.peppercorn: (ShopSource(items_price=((15, Fossil.bone_fragment)), shop_region=Region.island_trader),),



        },
    ))

register_mod_content_pack(CornCropExtContentPack(
    ModNames.cornucopia_crop,
    harvest_sources={
        CornCropExtForageable.chickwood: (HarvestCropSource(seed=CornCropExtSapling.chickwood, seasons=(Season.summer, Season.fall)), ForagingSource(regions=(Region.secret_woods,), seasons=(Season.fall,),)), 
        CornCropExtForageable.shiitake: (HarvestCropSource(seed=CornCropExtSapling.shiitake, seasons=(Season.spring, Season.fall)),),
        CornCropExtFlower.canola: (Tag(ItemTag.FLOWER), HarvestCropSource(seed=CornCropExtSeed.canola, seasons=(Season.spring, Season.summer)),),
        CornCropExtFruit.canary_melon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSeed.canary_melon, seasons=(Season.spring,)),),
        CornCropExtFruit.cantaloupe: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSeed.cantaloupe, seasons=(Season.spring,)),),
        CornCropExtFruit.groundcherry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSeed.groundcherry, seasons=(Season.summer, Season.fall)),),
        CornCropExtFruit.habanero: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSeed.habanero, seasons=(Season.fall,)),),
        CornCropExtFruit.honeydew: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSeed.honeydew, seasons=(Season.summer,)),),
        CornCropExtFruit.jalapeno: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSeed.jalapeno, seasons=(Season.spring,)),),
        CornCropExtFruit.passion_fruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSeed.passion_fruit, seasons=(Season.spring,)),),
        CornCropExtFruit.currant: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornSapling.currant, seasons=(Season.summer,)),),
        CornCropExtFruit.elderberry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSapling.elderberry, seasons=(Season.winter,)),),
        CornCropExtFruit.gooseberry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSapling.gooseberry, seasons=(Season.summer,)),),
        CornCropExtFruit.juniper: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSapling.juniper, seasons=(Season.winter,)), ForagingSource(regions=(Region.forest, Region.mountain), seasons=(Season.spring,),)),
        CornCropExtFruit.white_grape: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSapling.white_grape, seasons=(Season.fall,)),),
        CornCropExtFruit.sapodilla: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornCropExtSapling.sapodilla, seasons=(Season.summer,)),),
        CornCropExtVegetable.adzuki: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.adzuki, seasons=(Season.summer,)),),
        CornCropExtVegetable.agave: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.sapodilla, seasons=(Season.spring,)),),
        CornCropExtVegetable.asparagus: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.asparagus, seasons=(Season.spring,)),),
        CornCropExtVegetable.bamboo: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.bamboo, seasons=(Season.summer,)),),
        CornCropExtVegetable.barley: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.barley, seasons=(Season.fall,)),),
        CornCropExtVegetable.black_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.black_bean, seasons=(Season.fall,)),),
        CornCropExtVegetable.blue_agave: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.blue_agave, seasons=(Season.summer,)),),
        CornCropExtVegetable.buckwheat: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.buckwheat, seasons=(Season.spring,)),),
        CornCropExtVegetable.butternut_squash: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.butternut_squash, seasons=(Season.summer,)),),
        CornCropExtVegetable.cabbage: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.cabbage, seasons=(Season.spring,)),),
        CornCropExtVegetable.cassava: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.cassava, seasons=(Season.summer,)),),
        CornCropExtVegetable.celery: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.celery, seasons=(Season.fall,)),),
        CornCropExtVegetable.chickpea: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.chickpea, seasons=(Season.summer,)),),
        CornCropExtVegetable.daikon: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.daikon, seasons=(Season.fall,)),),
        CornCropExtVegetable.durum: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.durum, seasons=(Season.fall,)),),
        CornCropExtVegetable.ginseng: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.ginseng, seasons=(Season.spring, Season.winter)),),
        CornCropExtVegetable.green_pea: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.green_pea, seasons=(Season.summer,)),),
        CornCropExtVegetable.kidney_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.kidney_bean, seasons=(Season.fall,)),),
        CornCropExtVegetable.navy_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.navy_bean, seasons=(Season.summer,)),),
        CornCropExtVegetable.oat: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.oat, seasons=(Season.fall,)),),
        CornCropExtVegetable.okra: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.okra, seasons=(Season.summer, Season.fall)),),
        CornCropExtVegetable.pinto_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.pinto_bean, seasons=(Season.spring,)),),
        CornCropExtVegetable.quinoa: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.quinoa, seasons=(Season.summer,)),),
        CornCropExtVegetable.red_onion: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.red_onion, seasons=(Season.spring,)),),
        CornCropExtVegetable.shallot: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.shallot, seasons=(Season.spring,)),),
        CornCropExtVegetable.sugar_beet: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.sugar_beet, seasons=(Season.spring,)),),
        CornCropExtVegetable.sweet_potato: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.sweet_potato, seasons=(Season.fall,)),),
        CornCropExtVegetable.wasabi: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornCropExtSeed.wasabi, seasons=(Season.summer,)),),


        },
    shop_sources={
        CornCropExtSeed.adzuki: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornCropExtSeed.agave: (ShopSource(money_price=100, shop_region=Region.oasis, seasons=(Season.spring,)),),
        CornCropExtSeed.asparagus: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.bamboo: (ShopSource(money_price=80, shop_region=Region.oasis, seasons=(Season.summer, Season.spring)),),
        CornCropExtSeed.barley: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.black_bean: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.blue_agave: (ShopSource(money_price=180, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornCropExtSeed.buckwheat: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornCropExtSeed.butternut_squash: (ShopSource(money_price=180, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.cabbage: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornCropExtSeed.canary_melon: (ShopSource(money_price=450, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.canola: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.spring, Season.summer)),),
        CornCropExtSeed.cantaloupe: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.cassava: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.celery: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.chickpea: (ShopSource(money_price=200, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.daikon: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornCropExtSeed.durum: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.ginseng: (ShopSource(items_price=((4, CornVegetable.turnip),), shop_region=LogicRegion.mines_dwarf_shop)),
        CornCropExtSeed.green_pea: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornCropExtSeed.groundcherry: (ShopSource(money_price=150, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall)),),
        CornCropExtSeed.habanero: (ShopSource(money_price=130, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.honeydew: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.jalapeno: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.kidney_bean: (ShopSource(money_price=180, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.navy_bean: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornCropExtSeed.oat: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.okra: (ShopSource(money_price=160, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.passion_fruit: (ShopSource(items_price=((3, WaterItem.coral),), shop_region=Region.island_trader),),
        CornCropExtSeed.pinto: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.quinoa: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.red_onion: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.shallot: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornCropExtSeed.sugar_beet: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornCropExtSeed.sweet_potato: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornCropExtSeed.wasabi: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)), ShopSource(money_price=100, shop_region=LogicRegion.egg_festival)),
        CornCropExtSapling.white_grape: (ShopSource(money_price=600, shop_region=Region.pierre_store),),
        CornCropExtSapling.currant: (ShopSource(money_price=850, shop_region=Region.pierre_store),),
        CornCropExtSapling.chickwood: (ShopSource(money_price=1200, shop_region=Region.mines_dwarf_shop),),
        CornCropExtSapling.elderberry: (ShopSource(money_price=700, shop_region=Region.pierre_store),),
        CornCropExtSapling.gooseberry: (ShopSource(money_price=1000, shop_region=Region.pierre_store),),
        CornCropExtSapling.juniper: (ShopSource(money_price=400, shop_region=Region.pierre_store), ShopSource(money_price=200, shop_region=LogicRegion.festival_of_ice)),
        CornCropExtSapling.shiitake: (ShopSource(money_price=1000, shop_region=Region.mines_dwarf_shop),),
        CornCropExtSapling.sapodilla: (ShopSource(money_price=100, shop_region=LogicRegion.mines_dwarf_shop),),



        },
    ))

register_mod_content_pack(ContentPack(
    ModNames.cornucopia_herb,
        harvest_sources={
            CornHerbExtForageable.tumeric: (HarvestCropSource(seed=CornHerbExtSeed.tumeric, seasons=(Season.fall,)),),
            CornHerbExtForageable.cinnamon: (HarvestCropSource(seed=CornHerbExtSapling.cinnamon, seasons=(Season.winter,)),),
            CornHerbExtForageable.nutmeg: (HarvestCropSource(seed=CornHerbExtSapling.nutmeg, seasons=(Season.summer,)),),
            CornHerbExtVegetable.aloe: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.aloe, seasons=(Season.summer,)),),
            CornHerbExtVegetable.catnip: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.catnip, seasons=(Season.spring,)),),
            CornHerbExtVegetable.chives: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.chives, seasons=(Season.summer,)),),
            CornHerbExtVegetable.cilantro: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.cilantro, seasons=(Season.fall,)),),
            CornHerbExtVegetable.dill: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.dill, seasons=(Season.spring,)),),
            CornHerbExtVegetable.fennel: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.fennel, seasons=(Season.fall,)),),
            CornHerbExtVegetable.fenugreek: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.fenugreek, seasons=(Season.spring,)),),
            CornHerbExtVegetable.lemongrass: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.lemongrass, seasons=(Season.summer,)),),
            CornHerbExtVegetable.licorice_root: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.licorice_root, seasons=(Season.spring,)),),
            CornHerbExtVegetable.majoram: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.majoram, seasons=(Season.spring,)),),
            CornHerbExtVegetable.mint: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.mint, seasons=(Season.winter,)),),
            CornHerbExtVegetable.oregano: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.oregano, seasons=(Season.summer,)),),
            CornHerbExtVegetable.parsley: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.parsley, seasons=(Season.spring,)),),
            CornHerbExtVegetable.perilla: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.perilla, seasons=(Season.summer,)),),
            CornHerbExtVegetable.rosemary: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.rosemary, seasons=(Season.fall,)),),
            CornHerbExtVegetable.sage: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.sage, seasons=(Season.fall,)),),
            CornHerbExtVegetable.tarragon: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.tarragon, seasons=(Season.fall,)),),
            CornHerbExtVegetable.thyme: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.thyme, seasons=(Season.fall,)),),
            CornHerbExtVegetable.wormwood: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSeed.wormwood, seasons=(Season.winter,)),),
            CornHerbExtVegetable.bay: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSapling.bay, seasons=(Season.winter,)),),
            CornHerbExtVegetable.camphor: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSapling.camphor, seasons=(Season.winter,)),),
            CornHerbExtVegetable.eucalyptus: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSapling.eucalyptus, seasons=(Season.spring,)),),
            CornHerbExtVegetable.melaleuca: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornHerbExtSapling.melaleuca, seasons=(Season.spring,)),),



        },
    shop_sources={
        CornHerbExtSeed.aloe: (ShopSource(money_price=100, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornHerbExtSeed.catnip: (ShopSource(money_price=60, shop_region=Region.ranch, seasons=(Season.spring,)),),
        CornHerbExtSeed.chive: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.cilantro: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.cumin_starter: (ShopSource(money_price=80, shop_region=Region.oasis, seasons=(Season.fall,)),),
        CornHerbExtSeed.dill: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornHerbExtSeed.fennel: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.fenugreek: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.lemongrass: (ShopSource(money_price=20, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornHerbExtSeed.licorice_root: (ShopSource(money_price=100, shop_region=LogicRegion.mines_dwarf_shop, seasons=(Season.spring,)),),
        CornHerbExtSeed.majoram: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.mint: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.winter,)),),
        CornHerbExtSeed.oregano: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.parsley: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornHerbExtSeed.perilla: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.rosemary: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornHerbExtSeed.sage: (ShopSource(money_price=40, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornHerbExtSeed.tarragon: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.thyme: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornHerbExtSeed.wormwood: (ShopSource(money_price=100, shop_region=LogicRegion.mines_dwarf_shop, seasons=(Season.winter,)),),
        CornHerbExtSapling.bay: (ShopSource(money_price=650, shop_region=Region.pierre_store),),
        CornHerbExtSapling.camphor: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        CornHerbExtSapling.cinnamon: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),
        CornHerbExtSapling.eucalyptus: (ShopSource(money_price=5500, shop_region=Region.pierre_store),),
        CornHerbExtSapling.melaleuca: (ShopSource(money_price=650, shop_region=Region.pierre_store),),
        CornHerbExtSapling.nutmeg: (ShopSource(money_price=4000, shop_region=Region.ranch),),
        },
    ))

register_mod_content_pack(CornTreeExtContentPack(
    ModNames.cornucopia_tree,
        harvest_sources={
            CornTreeExtForageable.almond: (HarvestCropSource(seed=CornTreeExtSapling.almond, seasons=(Season.fall,)),),
            CornTreeExtForageable.cashew: (HarvestCropSource(seed=CornTreeExtSapling.cashew, seasons=(Season.fall,)),),
            CornTreeExtForageable.pecan: (HarvestCropSource(seed=CornTreeExtSapling.pecan, seasons=(Season.fall,)),),
            CornTreeExtForageable.walnut: (HarvestCropSource(seed=CornTreeExtSapling.walnut, seasons=(Season.fall,)),),
            CornTreeExtFruit.breadfruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.breadfruit, seasons=(Season.spring,)),),
            CornTreeExtFruit.dragon_fruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.dragon_fruit, seasons=(Season.summer,)),),
            CornTreeExtFruit.durian: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.durian, seasons=(Season.summer,)),),
            CornTreeExtFruit.fig: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.fig, seasons=(Season.winter,)),),
            CornTreeExtFruit.grapefruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.grapefruit, seasons=(Season.fall,)),),
            CornTreeExtFruit.lemon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.lemon, seasons=(Season.spring,)),),
            CornTreeExtFruit.lime: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.lime, seasons=(Season.spring,)),),
            CornTreeExtFruit.lychee: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.lychee, seasons=(Season.summer,)),),
            CornTreeExtFruit.nectarine: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.nectarine, seasons=(Season.summer,)),),
            CornTreeExtFruit.persimmon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.persimmon, seasons=(Season.winter,)),),
            CornTreeExtFruit.papaya: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.papaya, seasons=(Season.summer,)),),
            CornTreeExtFruit.plantain: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.plantain, seasons=(Season.summer,)),),
            CornTreeExtFruit.pomelo: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.pomelo, seasons=(Season.fall,)),),
            CornTreeExtFruit.ume: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.ume, seasons=(Season.summer,)),),
            CornTreeExtFruit.yuzu: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornTreeExtSapling.yuzu, seasons=(Season.winter,)),),


        },
    shop_sources={
        CornTreeExtSapling.almond: (ShopSource(money_price=3750, shop_region=Region.pierre_store),),
        CornTreeExtSapling.breadfruit: (ShopSource(money_price=8000, shop_region=Region.oasis),),
        CornTreeExtSapling.cashew: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.dragon_fruit: (ShopSource(money_price=5000, shop_region=Region.oasis),),
        CornTreeExtSapling.durian: (ShopSource(items_price=((20, WaterItem.sea_urchin),), shop_region=Region.island_trader),),
        CornTreeExtSapling.fig: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.grapefruit: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.lemon: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.lime: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.lychee: (ShopSource(money_price=5000, shop_region=Region.oasis),),
        CornTreeExtSapling.nectarine: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.papaya: (ShopSource(items_price=((5, Fish.lionfish),), shop_region=Region.island_trader),),
        CornTreeExtSapling.pecan: (ShopSource(money_price=5000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.persimmon: (ShopSource(money_price=7000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.plantain: (ShopSource(items_price=((5, Fruit.banana),), shop_region=Region.island_trader),),
        CornTreeExtSapling.pomelo: (ShopSource(money_price=3400, shop_region=Region.pierre_store),),
        CornTreeExtSapling.ume: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornTreeExtSapling.walnut: (ShopSource(money_price=3750, shop_region=Region.pierre_store),),
        CornTreeExtSapling.yuzu: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),



        },
    ))