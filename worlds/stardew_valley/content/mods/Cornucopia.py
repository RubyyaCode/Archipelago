from ..game_content import ContentPack, StardewContent
from ..mod_registry import register_mod_content_pack
from ..override import override
from ...data.harvest import ForagingSource, HarvestFruitTreeSource, HarvestCropSource
from ...data.requirement import YearRequirement, SeasonRequirement
from ...mods.mod_data import ModNames
from ...strings.crop_names import CornucopiaCropsFruit, CornucopiaCropsVegetable, CornucopiaCropsExtendedCropsFruit, CornucopiaCropsExtendedCropsVegetable, CornucopiaCropsExtendedHerbsVegetable, CornucopiaCropsExtendedTreesFruit, Fruit
from ...strings.flower_names import CornucopiaCropsFlower, CornucopiaCropsExtendedCropsFlower, Flower
from ...strings.forageable_names import CornucopiaCropsForageable, CornucopiaCropsExtendedCropsForageable, CornucopiaCropsExtendedTreesForageable, CornucopiaCropsExtendedHerbsForageable, Forageable
from ...strings.fruit_tree_names import CornucopiaCropsSapling, CornucopiaCropsExtendedCropsSapling, CornucopiaCropsExtendedHerbsSapling, CornucopiaCropsExtendedTreesSapling
from ...strings.season_names import Season
from ...strings.region_names import Region
from ..vanilla.ginger_island import ginger_island_content_pack as ginger_island_content_pack
from ...strings.seed_names import CornucopiaCropsSeed, CornucopiaCropsExtendedCropsSeed, CornucopiaCropsExtendedHerbsSeed
from ...data.game_item import ItemTag, ItemSource, Tag
from ...data.shop import ShopSource
from ...strings.generic_names import Generic
from ...strings.material_names import Material
from ...strings.region_names import Region, LogicRegion
from ...strings.currency_names import Currency
from ...strings.fish_names import Fish, WaterItem
from ...strings.metal_names import Fossil
#from ...data import flower_names, crop_names, seed_names, fruit_tree_names, forageable_names








class CornucopiaCropsContentPack(ContentPack):
    def crop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.harvest_sources.pop(CornucopiaCropsFlower.vanilla.name)
            content.harvest_sources.pop(CornucopiaCropsVegetable.peppercorn.name)
            
    def shop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.shop_sources.pop(CornucopiaCropsSapling.vanilla.name)
            content.shop_sources.pop(CornucopiaCropsSapling.peppercorn.name)
            
class CornucopiaCropsExtendedCropsContentPack(ContentPack):
    def crop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.harvest_sources.pop(CornucopiaCropsExtendedCropsFruit.passion_fruit.name)
            
    def shop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.shop_sources.pop(CornucopiaCropsExtendedCropsSeed.passion_fruit.name)

class CornucopiaCropsExtendedTreesContentPack(ContentPack):
    def crop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.harvest_sources.pop(CornucopiaCropsExtendedTreesFruit.durian.name)
            content.harvest_sources.pop(CornucopiaCropsExtendedTreesFruit.papaya.name)
            content.harvest_sources.pop(CornucopiaCropsExtendedTreesFruit.plantain.name)
            
    def shop_hook(self, content: StardewContent):
        if ginger_island_content_pack.name not in content.registered_packs:
            content.shop_sources.pop(CornucopiaCropsExtendedTreesSapling.durian.name)
            content.shop_sources.pop(CornucopiaCropsExtendedTreesSapling.papaya.name)
            content.shop_sources.pop(CornucopiaCropsExtendedTreesSapling.plantain.name)
  




register_mod_content_pack(CornucopiaCropsContentPack(
    ModNames.cornucopia_crops,
   
    harvest_sources={
        CornucopiaCropsVegetable.basil: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.basil, seasons=(Season.spring,)),),
        CornucopiaCropsVegetable.cucumber: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.cucumber, seasons=(Season.summer,)),),
        CornucopiaCropsVegetable.lettuce: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.lettuce, seasons=(Season.summer,)),),
        CornucopiaCropsVegetable.onion: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.onion, seasons=(Season.spring,)),),
        CornucopiaCropsVegetable.peanut: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.peanut, seasons=(Season.fall,)),),
        CornucopiaCropsVegetable.spinach: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.spinach, seasons=(Season.spring, Season.fall)),),
        CornucopiaCropsVegetable.sugarcane: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.sugarcane, seasons=(Season.summer,)),),
        CornucopiaCropsVegetable.turnip: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.turnip, seasons=(Season.fall,)),),
        CornucopiaCropsVegetable.zucchini: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSeed.zucchini, seasons=(Season.fall,)),),
        CornucopiaCropsVegetable.olive: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSapling.olive, seasons=(Season.fall,)),),
        CornucopiaCropsFruit.bell_pepper: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsSeed.bell_pepper, seasons=(Season.summer,)),),
        CornucopiaCropsFruit.kiwi: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsSeed.kiwi, seasons=(Season.summer,)),),
        CornucopiaCropsFruit.watermelon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsSeed.watermelon, seasons=(Season.summer,)),),
        CornucopiaCropsFruit.avocado: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsSapling.avocado, seasons=(Season.summer,)),),
        CornucopiaCropsFruit.pear: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsSapling.pear, seasons=(Season.winter,)),),
        CornucopiaCropsFruit.raspberry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsSapling.raspberry, seasons=(Season.summer,)), ForagingSource(regions=(Region.forest, Region.mountain, Region.town), season=(Season.summer,))),
        CornucopiaCropsForageable.cotton: (HarvestCropSource(seed=CornucopiaCropsSeed.cotton, seasons=(Season.summer, Season.fall)),),
        CornucopiaCropsForageable.cocoa: (HarvestCropSource(seed=CornucopiaCropsSapling.cocoa, seasons=(Season.spring,)),),
        CornucopiaCropsForageable.pistachio: (HarvestCropSource(seed=CornucopiaCropsSapling.pistachio, seasons=(Season.fall,)),),
        CornucopiaCropsSeed.soybean: (HarvestCropSource(seed=CornucopiaCropsSeed.soybean_starter, seasons=(Season.fall,)),),
        CornucopiaCropsFlower.vanilla: (Tag(ItemTag.FLOWER), HarvestCropSource(seed=CornucopiaCropsSapling.vanilla, seasons=(Season.spring,)),),
        CornucopiaCropsVegetable.peppercorn: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsSapling.peppercorn, seasons=(Season.spring, Season.summer, Season.fall)), ForagingSource(regions=(Region.forest, Region.mountain), seasons=(Season.spring,),), ForagingSource(regions=(Region.island_east, Region.island_west, Region.island_south))),
         
        
        },
    shop_sources={
        CornucopiaCropsSeed.cotton: (ShopSource(money_price=200, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall)), ShopSource(items_price=((250, Currency.star_token),), shop_region=LogicRegion.fair),),
        CornucopiaCropsSapling.cocoa: (ShopSource(money_price=5000, shop_region=Region.pierre_store),),
        CornucopiaCropsSapling.pistachio: (ShopSource(money_price=3750, shop_region=Region.pierre_store),),
        CornucopiaCropsSeed.soybean_starter: (ShopSource(money_price=2000, shop_region=LogicRegion.traveling_cart, seasons=(Season.fall,),),),
        CornucopiaCropsSeed.bell_pepper: (ShopSource(money_price=130, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornucopiaCropsSeed.basil: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornucopiaCropsSeed.turnip: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornucopiaCropsSeed.cucumber: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsSeed.kiwi: (ShopSource(money_price=100, shop_region=LogicRegion.luau), ShopSource(items_price=((1, Fish.tuna),), shop_region=Region.island_trader),),
        CornucopiaCropsSeed.lettuce: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornucopiaCropsSeed.onion: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornucopiaCropsSeed.peanut: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornucopiaCropsSeed.spinach: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.spring, Season.fall)),),
        CornucopiaCropsSeed.sugarcane: (ShopSource(money_price=20, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornucopiaCropsSeed.watermelon: (ShopSource(money_price=300, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)), ShopSource(money_price=300, shop_region=LogicRegion.luau),),
        CornucopiaCropsSeed.zucchini: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsSapling.olive: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornucopiaCropsSapling.raspberry: (ShopSource(money_price=500, shop_region=Region.pierre_store),),
        CornucopiaCropsSapling.avocado: (ShopSource(money_price=8000, shop_region=Region.pierre_store),),
        CornucopiaCropsSapling.pear: (ShopSource(money_price=5500, shop_region=Region.pierre_store),),
        CornucopiaCropsSapling.vanilla: (ShopSource(items_price=((1, Forageable.rainbow_shell),), shop_region=Region.island_trader),),
        CornucopiaCropsSapling.peppercorn: (ShopSource(items_price=((15, Fossil.bone_fragment)), shop_region=Region.island_trader),),



        },
    ))

register_mod_content_pack(CornucopiaCropsExtendedCropsContentPack(
    ModNames.cornucopia_crops_crops,
    harvest_sources={
        CornucopiaCropsExtendedCropsForageable.chickwood: (HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.chickwood, seasons=(Season.summer, Season.fall)), ForagingSource(regions=(Region.secret_woods,), seasons=(Season.fall,),)), 
        CornucopiaCropsExtendedCropsForageable.shiitake: (HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.shiitake, seasons=(Season.spring, Season.fall)),),
        CornucopiaCropsExtendedCropsFlower.canola: (Tag(ItemTag.FLOWER), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.canola, seasons=(Season.spring, Season.summer)),),
        CornucopiaCropsExtendedCropsFruit.canary_melon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.canary_melon, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsFruit.cantaloupe: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.cantaloupe, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsFruit.groundcherry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.groundcherry, seasons=(Season.summer, Season.fall)),),
        CornucopiaCropsExtendedCropsFruit.habanero: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.habanero, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsFruit.honeydew: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.honeydew, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsFruit.jalapeno: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.jalapeno, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsFruit.passion_fruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.passion_fruit, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsFruit.currant: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.currant, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsFruit.elderberry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.elderberry, seasons=(Season.winter,)),),
        CornucopiaCropsExtendedCropsFruit.gooseberry: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.gooseberry, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsFruit.juniper: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.juniper, seasons=(Season.winter,)), ForagingSource(regions=(Region.forest, Region.mountain), seasons=(Season.spring,),)),
        CornucopiaCropsExtendedCropsFruit.white_grape: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.white_grape, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsFruit.sapodilla: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.sapodilla, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.adzuki: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.adzuki, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.agave: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSapling.sapodilla, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.asparagus: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.asparagus, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.bamboo: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.bamboo, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.barley: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.barley, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.black_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.black_bean, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.blue_agave: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.blue_agave, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.buckwheat: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.buckwheat, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.butternut_squash: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.butternut_squash, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.cabbage: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.cabbage, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.cassava: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.cassava, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.celery: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.celery, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.chickpea: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.chickpea, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.daikon: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.daikon, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.durum: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.durum, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.ginseng: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.ginseng, seasons=(Season.spring, Season.winter)),),
        CornucopiaCropsExtendedCropsVegetable.green_pea: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.green_pea, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.kidney_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.kidney_bean, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.navy_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.navy_bean, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.oat: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.oat, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.okra: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.okra, seasons=(Season.summer, Season.fall)),),
        CornucopiaCropsExtendedCropsVegetable.pinto_bean: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.pinto, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.quinoa: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.quinoa, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsVegetable.red_onion: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.red_onion, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.shallot: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.shallot, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.sugar_beet: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.sugar_beet, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsVegetable.sweet_potato: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.sweet_potato, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsVegetable.wasabi: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedCropsSeed.wasabi, seasons=(Season.summer,)),),


        },
    shop_sources={
        CornucopiaCropsExtendedCropsSeed.adzuki: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsSeed.agave: (ShopSource(money_price=100, shop_region=Region.oasis, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsSeed.asparagus: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.bamboo: (ShopSource(money_price=80, shop_region=Region.oasis, seasons=(Season.summer, Season.spring)),),
        CornucopiaCropsExtendedCropsSeed.barley: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.black_bean: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.blue_agave: (ShopSource(money_price=180, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsSeed.buckwheat: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsSeed.butternut_squash: (ShopSource(money_price=180, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.cabbage: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsSeed.canary_melon: (ShopSource(money_price=450, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.canola: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.spring, Season.summer)),),
        CornucopiaCropsExtendedCropsSeed.cantaloupe: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.cassava: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.celery: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.chickpea: (ShopSource(money_price=200, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.daikon: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsSeed.durum: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.ginseng: (ShopSource(items_price=((4, CornucopiaCropsVegetable.turnip),), shop_region=LogicRegion.mines_dwarf_shop)),
        CornucopiaCropsExtendedCropsSeed.green_pea: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsSeed.groundcherry: (ShopSource(money_price=150, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall)),),
        CornucopiaCropsExtendedCropsSeed.habanero: (ShopSource(money_price=130, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.honeydew: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.jalapeno: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.kidney_bean: (ShopSource(money_price=180, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.navy_bean: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedCropsSeed.oat: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.okra: (ShopSource(money_price=160, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.passion_fruit: (ShopSource(items_price=((3, WaterItem.coral),), shop_region=Region.island_trader),),
        CornucopiaCropsExtendedCropsSeed.pinto: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.quinoa: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.red_onion: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.shallot: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedCropsSeed.sugar_beet: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedCropsSeed.sweet_potato: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedCropsSeed.wasabi: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)), ShopSource(money_price=100, shop_region=LogicRegion.egg_festival)),
        CornucopiaCropsExtendedCropsSapling.white_grape: (ShopSource(money_price=600, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedCropsSapling.currant: (ShopSource(money_price=850, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedCropsSapling.chickwood: (ShopSource(money_price=1200, shop_region=LogicRegion.mines_dwarf_shop),),
        CornucopiaCropsExtendedCropsSapling.elderberry: (ShopSource(money_price=700, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedCropsSapling.gooseberry: (ShopSource(money_price=1000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedCropsSapling.juniper: (ShopSource(money_price=400, shop_region=Region.pierre_store), ShopSource(money_price=200, shop_region=LogicRegion.festival_of_ice)),
        CornucopiaCropsExtendedCropsSapling.shiitake: (ShopSource(money_price=1000, shop_region=LogicRegion.mines_dwarf_shop),),
        CornucopiaCropsExtendedCropsSapling.sapodilla: (ShopSource(money_price=100, shop_region=LogicRegion.mines_dwarf_shop),),



        },
    ))

register_mod_content_pack(ContentPack(
    ModNames.cornucopia_crops_herbs,
        harvest_sources={
            CornucopiaCropsExtendedHerbsForageable.turmeric: (HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.turmeric, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedHerbsForageable.cinnamon: (HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSapling.cinnamon, seasons=(Season.winter,)),),
            CornucopiaCropsExtendedHerbsForageable.nutmeg: (HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSapling.nutmeg, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedHerbsVegetable.aloe: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.aloe, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedHerbsVegetable.catnip: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.catnip, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedHerbsVegetable.chives: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.chive, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedHerbsVegetable.cilantro: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.cilantro, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedHerbsVegetable.dill: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.dill, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedHerbsVegetable.fennel: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.fennel, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedHerbsVegetable.fenugreek: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.fenugreek, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedHerbsVegetable.lemongrass: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.lemongrass, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedHerbsVegetable.licorice_root: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.licorice_root, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedHerbsVegetable.marjoram: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.marjoram, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedHerbsVegetable.mint: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.mint, seasons=(Season.winter,)),),
            CornucopiaCropsExtendedHerbsVegetable.oregano: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.oregano, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedHerbsVegetable.parsley: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.parsley, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedHerbsVegetable.perilla: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.perilla, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedHerbsVegetable.rosemary: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.rosemary, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedHerbsVegetable.sage: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.sage, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedHerbsVegetable.tarragon: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.tarragon, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedHerbsVegetable.thyme: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.thyme, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedHerbsVegetable.wormwood: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSeed.wormwood, seasons=(Season.winter,)),),
            CornucopiaCropsExtendedHerbsVegetable.bay: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSapling.bay, seasons=(Season.winter,)),),
            CornucopiaCropsExtendedHerbsVegetable.camphor: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSapling.camphor, seasons=(Season.winter,)),),
            CornucopiaCropsExtendedHerbsVegetable.eucalyptus: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSapling.eucalyptus, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedHerbsVegetable.melaleuca: (Tag(ItemTag.VEGETABLE), HarvestCropSource(seed=CornucopiaCropsExtendedHerbsSapling.melaleuca, seasons=(Season.spring,)),),



        },
    shop_sources={
        CornucopiaCropsExtendedHerbsSeed.aloe: (ShopSource(money_price=100, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedHerbsSeed.catnip: (ShopSource(money_price=60, shop_region=Region.ranch, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedHerbsSeed.chive: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.cilantro: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.cumin_starter: (ShopSource(money_price=80, shop_region=Region.oasis, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedHerbsSeed.dill: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedHerbsSeed.fennel: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.fenugreek: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.lemongrass: (ShopSource(money_price=20, shop_region=Region.oasis, seasons=(Season.summer,)),),
        CornucopiaCropsExtendedHerbsSeed.licorice_root: (ShopSource(money_price=100, shop_region=LogicRegion.mines_dwarf_shop, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedHerbsSeed.marjoram: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.spring,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.mint: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.winter,)),),
        CornucopiaCropsExtendedHerbsSeed.oregano: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.parsley: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        CornucopiaCropsExtendedHerbsSeed.perilla: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.summer,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.rosemary: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedHerbsSeed.sage: (ShopSource(money_price=40, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        CornucopiaCropsExtendedHerbsSeed.tarragon: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.thyme: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,), other_requirements=(YearRequirement(2),)),),
        CornucopiaCropsExtendedHerbsSeed.wormwood: (ShopSource(money_price=100, shop_region=LogicRegion.mines_dwarf_shop, seasons=(Season.winter,)),),
        CornucopiaCropsExtendedHerbsSapling.bay: (ShopSource(money_price=650, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedHerbsSapling.camphor: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedHerbsSapling.cinnamon: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedHerbsSapling.eucalyptus: (ShopSource(money_price=5500, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedHerbsSapling.melaleuca: (ShopSource(money_price=650, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedHerbsSapling.nutmeg: (ShopSource(money_price=4000, shop_region=Region.ranch),),
        },
    ))

register_mod_content_pack(CornucopiaCropsExtendedTreesContentPack(
    ModNames.cornucopia_crops_trees,
        harvest_sources={
            CornucopiaCropsExtendedTreesForageable.almond: (HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.almond, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedTreesForageable.cashew: (HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.cashew, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedTreesForageable.pecan: (HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.pecan, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedTreesForageable.walnut: (HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.walnut, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedTreesFruit.breadfruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.breadfruit, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedTreesFruit.dragon_fruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.dragon_fruit, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedTreesFruit.durian: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.durian, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedTreesFruit.fig: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.fig, seasons=(Season.winter,)),),
            CornucopiaCropsExtendedTreesFruit.grapefruit: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.grapefruit, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedTreesFruit.lemon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.lemon, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedTreesFruit.lime: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.lime, seasons=(Season.spring,)),),
            CornucopiaCropsExtendedTreesFruit.lychee: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.lychee, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedTreesFruit.nectarine: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.nectarine, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedTreesFruit.persimmon: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.persimmon, seasons=(Season.winter,)),),
            CornucopiaCropsExtendedTreesFruit.papaya: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.papaya, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedTreesFruit.plantain: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.plantain, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedTreesFruit.pomelo: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.pomelo, seasons=(Season.fall,)),),
            CornucopiaCropsExtendedTreesFruit.ume: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.ume, seasons=(Season.summer,)),),
            CornucopiaCropsExtendedTreesFruit.yuzu: (Tag(ItemTag.FRUIT), HarvestCropSource(seed=CornucopiaCropsExtendedTreesSapling.yuzu, seasons=(Season.winter,)),),


        },
    shop_sources={
        CornucopiaCropsExtendedTreesSapling.almond: (ShopSource(money_price=3750, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.breadfruit: (ShopSource(money_price=8000, shop_region=Region.oasis),),
        CornucopiaCropsExtendedTreesSapling.cashew: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.dragon_fruit: (ShopSource(money_price=5000, shop_region=Region.oasis),),
        CornucopiaCropsExtendedTreesSapling.durian: (ShopSource(items_price=((20, WaterItem.sea_urchin),), shop_region=Region.island_trader),),
        CornucopiaCropsExtendedTreesSapling.fig: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.grapefruit: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.lemon: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.lime: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.lychee: (ShopSource(money_price=5000, shop_region=Region.oasis),),
        CornucopiaCropsExtendedTreesSapling.nectarine: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.papaya: (ShopSource(items_price=((5, Fish.lionfish),), shop_region=Region.island_trader),),
        CornucopiaCropsExtendedTreesSapling.pecan: (ShopSource(money_price=5000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.persimmon: (ShopSource(money_price=7000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.plantain: (ShopSource(items_price=((5, Fruit.banana),), shop_region=Region.island_trader),),
        CornucopiaCropsExtendedTreesSapling.pomelo: (ShopSource(money_price=3400, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.ume: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.walnut: (ShopSource(money_price=3750, shop_region=Region.pierre_store),),
        CornucopiaCropsExtendedTreesSapling.yuzu: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),



        },
    ))