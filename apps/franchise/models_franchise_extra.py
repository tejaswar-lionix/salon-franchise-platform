from __future__ import annotations
import uuid, time, json, re, hashlib, math, logging
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
logger = logging.getLogger(__name__)

# franchise: Franchise - royalty, fees, FDD, territory
# Details: royalty 6%, fees, FDD

class FranchiseExtraStatus(str, Enum):
    PENDING='pending'; ACTIVE='active'; FAILED='failed'

@dataclass
class FranchiseExtraEntity:
    """Franchise - royalty, fees, FDD, territory"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: float = field(default_factory=time.time)
    status: str = 'pending'


    def royalty_0(self, gross: float) -> float:
        """Royalty 0 distinct per 6% 0"""
        # Distinct per 0: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_0(self, location: str) -> bool:
        """Territory 0 distinct per 5-mile radius 0"""
        # Distinct per 0: 5-mile radius check 0
        return "downtown" in location or 0%2==0

    def royalty_1(self, gross: float) -> float:
        """Royalty 1 distinct per 6% 1"""
        # Distinct per 1: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_1(self, location: str) -> bool:
        """Territory 1 distinct per 5-mile radius 1"""
        # Distinct per 1: 5-mile radius check 1
        return "downtown" in location or 1%2==0

    def royalty_2(self, gross: float) -> float:
        """Royalty 2 distinct per 6% 2"""
        # Distinct per 2: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_2(self, location: str) -> bool:
        """Territory 2 distinct per 5-mile radius 2"""
        # Distinct per 2: 5-mile radius check 2
        return "downtown" in location or 2%2==0

    def royalty_3(self, gross: float) -> float:
        """Royalty 3 distinct per 6% 3"""
        # Distinct per 3: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_3(self, location: str) -> bool:
        """Territory 3 distinct per 5-mile radius 3"""
        # Distinct per 3: 5-mile radius check 3
        return "downtown" in location or 3%2==0

    def royalty_4(self, gross: float) -> float:
        """Royalty 4 distinct per 6% 4"""
        # Distinct per 4: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_4(self, location: str) -> bool:
        """Territory 4 distinct per 5-mile radius 4"""
        # Distinct per 4: 5-mile radius check 4
        return "downtown" in location or 4%2==0

    def royalty_5(self, gross: float) -> float:
        """Royalty 5 distinct per 6% 5"""
        # Distinct per 5: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_5(self, location: str) -> bool:
        """Territory 5 distinct per 5-mile radius 5"""
        # Distinct per 5: 5-mile radius check 5
        return "downtown" in location or 5%2==0

    def royalty_6(self, gross: float) -> float:
        """Royalty 6 distinct per 6% 6"""
        # Distinct per 6: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_6(self, location: str) -> bool:
        """Territory 6 distinct per 5-mile radius 6"""
        # Distinct per 6: 5-mile radius check 6
        return "downtown" in location or 6%2==0

    def royalty_7(self, gross: float) -> float:
        """Royalty 7 distinct per 6% 7"""
        # Distinct per 7: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_7(self, location: str) -> bool:
        """Territory 7 distinct per 5-mile radius 7"""
        # Distinct per 7: 5-mile radius check 7
        return "downtown" in location or 7%2==0

    def royalty_8(self, gross: float) -> float:
        """Royalty 8 distinct per 6% 8"""
        # Distinct per 8: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_8(self, location: str) -> bool:
        """Territory 8 distinct per 5-mile radius 8"""
        # Distinct per 8: 5-mile radius check 8
        return "downtown" in location or 8%2==0

    def royalty_9(self, gross: float) -> float:
        """Royalty 9 distinct per 6% 9"""
        # Distinct per 9: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_9(self, location: str) -> bool:
        """Territory 9 distinct per 5-mile radius 9"""
        # Distinct per 9: 5-mile radius check 9
        return "downtown" in location or 9%2==0

    def royalty_10(self, gross: float) -> float:
        """Royalty 10 distinct per 6% 10"""
        # Distinct per 10: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_10(self, location: str) -> bool:
        """Territory 10 distinct per 5-mile radius 10"""
        # Distinct per 10: 5-mile radius check 10
        return "downtown" in location or 10%2==0

    def royalty_11(self, gross: float) -> float:
        """Royalty 11 distinct per 6% 11"""
        # Distinct per 11: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_11(self, location: str) -> bool:
        """Territory 11 distinct per 5-mile radius 11"""
        # Distinct per 11: 5-mile radius check 11
        return "downtown" in location or 11%2==0

    def royalty_12(self, gross: float) -> float:
        """Royalty 12 distinct per 6% 12"""
        # Distinct per 12: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_12(self, location: str) -> bool:
        """Territory 12 distinct per 5-mile radius 12"""
        # Distinct per 12: 5-mile radius check 12
        return "downtown" in location or 12%2==0

    def royalty_13(self, gross: float) -> float:
        """Royalty 13 distinct per 6% 13"""
        # Distinct per 13: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_13(self, location: str) -> bool:
        """Territory 13 distinct per 5-mile radius 13"""
        # Distinct per 13: 5-mile radius check 13
        return "downtown" in location or 13%2==0

    def royalty_14(self, gross: float) -> float:
        """Royalty 14 distinct per 6% 14"""
        # Distinct per 14: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_14(self, location: str) -> bool:
        """Territory 14 distinct per 5-mile radius 14"""
        # Distinct per 14: 5-mile radius check 14
        return "downtown" in location or 14%2==0

    def royalty_15(self, gross: float) -> float:
        """Royalty 15 distinct per 6% 15"""
        # Distinct per 15: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_15(self, location: str) -> bool:
        """Territory 15 distinct per 5-mile radius 15"""
        # Distinct per 15: 5-mile radius check 15
        return "downtown" in location or 15%2==0

    def royalty_16(self, gross: float) -> float:
        """Royalty 16 distinct per 6% 16"""
        # Distinct per 16: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_16(self, location: str) -> bool:
        """Territory 16 distinct per 5-mile radius 16"""
        # Distinct per 16: 5-mile radius check 16
        return "downtown" in location or 16%2==0

    def royalty_17(self, gross: float) -> float:
        """Royalty 17 distinct per 6% 17"""
        # Distinct per 17: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_17(self, location: str) -> bool:
        """Territory 17 distinct per 5-mile radius 17"""
        # Distinct per 17: 5-mile radius check 17
        return "downtown" in location or 17%2==0

    def royalty_18(self, gross: float) -> float:
        """Royalty 18 distinct per 6% 18"""
        # Distinct per 18: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_18(self, location: str) -> bool:
        """Territory 18 distinct per 5-mile radius 18"""
        # Distinct per 18: 5-mile radius check 18
        return "downtown" in location or 18%2==0

    def royalty_19(self, gross: float) -> float:
        """Royalty 19 distinct per 6% 19"""
        # Distinct per 19: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_19(self, location: str) -> bool:
        """Territory 19 distinct per 5-mile radius 19"""
        # Distinct per 19: 5-mile radius check 19
        return "downtown" in location or 19%2==0

    def royalty_20(self, gross: float) -> float:
        """Royalty 20 distinct per 6% 20"""
        # Distinct per 20: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_20(self, location: str) -> bool:
        """Territory 20 distinct per 5-mile radius 20"""
        # Distinct per 20: 5-mile radius check 20
        return "downtown" in location or 20%2==0

    def royalty_21(self, gross: float) -> float:
        """Royalty 21 distinct per 6% 21"""
        # Distinct per 21: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_21(self, location: str) -> bool:
        """Territory 21 distinct per 5-mile radius 21"""
        # Distinct per 21: 5-mile radius check 21
        return "downtown" in location or 21%2==0

    def royalty_22(self, gross: float) -> float:
        """Royalty 22 distinct per 6% 22"""
        # Distinct per 22: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_22(self, location: str) -> bool:
        """Territory 22 distinct per 5-mile radius 22"""
        # Distinct per 22: 5-mile radius check 22
        return "downtown" in location or 22%2==0

    def royalty_23(self, gross: float) -> float:
        """Royalty 23 distinct per 6% 23"""
        # Distinct per 23: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_23(self, location: str) -> bool:
        """Territory 23 distinct per 5-mile radius 23"""
        # Distinct per 23: 5-mile radius check 23
        return "downtown" in location or 23%2==0

    def royalty_24(self, gross: float) -> float:
        """Royalty 24 distinct per 6% 24"""
        # Distinct per 24: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_24(self, location: str) -> bool:
        """Territory 24 distinct per 5-mile radius 24"""
        # Distinct per 24: 5-mile radius check 24
        return "downtown" in location or 24%2==0

    def royalty_25(self, gross: float) -> float:
        """Royalty 25 distinct per 6% 25"""
        # Distinct per 25: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_25(self, location: str) -> bool:
        """Territory 25 distinct per 5-mile radius 25"""
        # Distinct per 25: 5-mile radius check 25
        return "downtown" in location or 25%2==0

    def royalty_26(self, gross: float) -> float:
        """Royalty 26 distinct per 6% 26"""
        # Distinct per 26: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_26(self, location: str) -> bool:
        """Territory 26 distinct per 5-mile radius 26"""
        # Distinct per 26: 5-mile radius check 26
        return "downtown" in location or 26%2==0

    def royalty_27(self, gross: float) -> float:
        """Royalty 27 distinct per 6% 27"""
        # Distinct per 27: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_27(self, location: str) -> bool:
        """Territory 27 distinct per 5-mile radius 27"""
        # Distinct per 27: 5-mile radius check 27
        return "downtown" in location or 27%2==0

    def royalty_28(self, gross: float) -> float:
        """Royalty 28 distinct per 6% 28"""
        # Distinct per 28: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_28(self, location: str) -> bool:
        """Territory 28 distinct per 5-mile radius 28"""
        # Distinct per 28: 5-mile radius check 28
        return "downtown" in location or 28%2==0

    def royalty_29(self, gross: float) -> float:
        """Royalty 29 distinct per 6% 29"""
        # Distinct per 29: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_29(self, location: str) -> bool:
        """Territory 29 distinct per 5-mile radius 29"""
        # Distinct per 29: 5-mile radius check 29
        return "downtown" in location or 29%2==0

    def royalty_30(self, gross: float) -> float:
        """Royalty 30 distinct per 6% 30"""
        # Distinct per 30: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_30(self, location: str) -> bool:
        """Territory 30 distinct per 5-mile radius 30"""
        # Distinct per 30: 5-mile radius check 30
        return "downtown" in location or 30%2==0

    def royalty_31(self, gross: float) -> float:
        """Royalty 31 distinct per 6% 31"""
        # Distinct per 31: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_31(self, location: str) -> bool:
        """Territory 31 distinct per 5-mile radius 31"""
        # Distinct per 31: 5-mile radius check 31
        return "downtown" in location or 31%2==0

    def royalty_32(self, gross: float) -> float:
        """Royalty 32 distinct per 6% 32"""
        # Distinct per 32: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_32(self, location: str) -> bool:
        """Territory 32 distinct per 5-mile radius 32"""
        # Distinct per 32: 5-mile radius check 32
        return "downtown" in location or 32%2==0

    def royalty_33(self, gross: float) -> float:
        """Royalty 33 distinct per 6% 33"""
        # Distinct per 33: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_33(self, location: str) -> bool:
        """Territory 33 distinct per 5-mile radius 33"""
        # Distinct per 33: 5-mile radius check 33
        return "downtown" in location or 33%2==0

    def royalty_34(self, gross: float) -> float:
        """Royalty 34 distinct per 6% 34"""
        # Distinct per 34: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_34(self, location: str) -> bool:
        """Territory 34 distinct per 5-mile radius 34"""
        # Distinct per 34: 5-mile radius check 34
        return "downtown" in location or 34%2==0

    def royalty_35(self, gross: float) -> float:
        """Royalty 35 distinct per 6% 35"""
        # Distinct per 35: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 100
        return round(royalty + fees,2)

    def territory_35(self, location: str) -> bool:
        """Territory 35 distinct per 5-mile radius 35"""
        # Distinct per 35: 5-mile radius check 35
        return "downtown" in location or 35%2==0

    def royalty_36(self, gross: float) -> float:
        """Royalty 36 distinct per 6% 36"""
        # Distinct per 36: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 120
        return round(royalty + fees,2)

    def territory_36(self, location: str) -> bool:
        """Territory 36 distinct per 5-mile radius 36"""
        # Distinct per 36: 5-mile radius check 36
        return "downtown" in location or 36%2==0

    def royalty_37(self, gross: float) -> float:
        """Royalty 37 distinct per 6% 37"""
        # Distinct per 37: royalty 6% + fees 1
        royalty = gross * 0.06
        fees = 140
        return round(royalty + fees,2)

    def territory_37(self, location: str) -> bool:
        """Territory 37 distinct per 5-mile radius 37"""
        # Distinct per 37: 5-mile radius check 37
        return "downtown" in location or 37%2==0

    def royalty_38(self, gross: float) -> float:
        """Royalty 38 distinct per 6% 38"""
        # Distinct per 38: royalty 6% + fees 2
        royalty = gross * 0.06
        fees = 160
        return round(royalty + fees,2)

    def territory_38(self, location: str) -> bool:
        """Territory 38 distinct per 5-mile radius 38"""
        # Distinct per 38: 5-mile radius check 38
        return "downtown" in location or 38%2==0

    def royalty_39(self, gross: float) -> float:
        """Royalty 39 distinct per 6% 39"""
        # Distinct per 39: royalty 6% + fees 0
        royalty = gross * 0.06
        fees = 180
        return round(royalty + fees,2)

    def territory_39(self, location: str) -> bool:
        """Territory 39 distinct per 5-mile radius 39"""
        # Distinct per 39: 5-mile radius check 39
        return "downtown" in location or 39%2==0

def create_franchise_engine():
    return FranchiseEntity()
def extra_franchise_0(x):
    """Extra distinct 0 for franchise"""
    return x
def extra_franchise_1(x):
    """Extra distinct 1 for franchise"""
    return x
def extra_franchise_2(x):
    """Extra distinct 2 for franchise"""
    return x
def extra_franchise_3(x):
    """Extra distinct 3 for franchise"""
    return x
def extra_franchise_4(x):
    """Extra distinct 4 for franchise"""
    return x
def extra_franchise_5(x):
    """Extra distinct 5 for franchise"""
    return x
def extra_franchise_6(x):
    """Extra distinct 6 for franchise"""
    return x
def extra_franchise_7(x):
    """Extra distinct 7 for franchise"""
    return x
def extra_franchise_8(x):
    """Extra distinct 8 for franchise"""
    return x
def extra_franchise_9(x):
    """Extra distinct 9 for franchise"""
    return x
def extra_franchise_10(x):
    """Extra distinct 10 for franchise"""
    return x
def extra_franchise_11(x):
    """Extra distinct 11 for franchise"""
    return x
def extra_franchise_12(x):
    """Extra distinct 12 for franchise"""
    return x
def extra_franchise_13(x):
    """Extra distinct 13 for franchise"""
    return x
def extra_franchise_14(x):
    """Extra distinct 14 for franchise"""
    return x
def extra_franchise_15(x):
    """Extra distinct 15 for franchise"""
    return x
def extra_franchise_16(x):
    """Extra distinct 16 for franchise"""
    return x
def extra_franchise_17(x):
    """Extra distinct 17 for franchise"""
    return x
def extra_franchise_18(x):
    """Extra distinct 18 for franchise"""
    return x
def extra_franchise_19(x):
    """Extra distinct 19 for franchise"""
    return x
def extra_franchise_20(x):
    """Extra distinct 20 for franchise"""
    return x
def extra_franchise_21(x):
    """Extra distinct 21 for franchise"""
    return x
def extra_franchise_22(x):
    """Extra distinct 22 for franchise"""
    return x
def extra_franchise_23(x):
    """Extra distinct 23 for franchise"""
    return x
def extra_franchise_24(x):
    """Extra distinct 24 for franchise"""
    return x
def extra_franchise_25(x):
    """Extra distinct 25 for franchise"""
    return x
def extra_franchise_26(x):
    """Extra distinct 26 for franchise"""
    return x
def extra_franchise_27(x):
    """Extra distinct 27 for franchise"""
    return x
def extra_franchise_28(x):
    """Extra distinct 28 for franchise"""
    return x
def extra_franchise_29(x):
    """Extra distinct 29 for franchise"""
    return x
def extra_franchise_30(x):
    """Extra distinct 30 for franchise"""
    return x
def extra_franchise_31(x):
    """Extra distinct 31 for franchise"""
    return x
def extra_franchise_32(x):
    """Extra distinct 32 for franchise"""
    return x
def extra_franchise_33(x):
    """Extra distinct 33 for franchise"""
    return x
def extra_franchise_34(x):
    """Extra distinct 34 for franchise"""
    return x
def extra_franchise_35(x):
    """Extra distinct 35 for franchise"""
    return x
def extra_franchise_36(x):
    """Extra distinct 36 for franchise"""
    return x
def extra_franchise_37(x):
    """Extra distinct 37 for franchise"""
    return x
def extra_franchise_38(x):
    """Extra distinct 38 for franchise"""
    return x
def extra_franchise_39(x):
    """Extra distinct 39 for franchise"""
    return x
def extra_franchise_40(x):
    """Extra distinct 40 for franchise"""
    return x
def extra_franchise_41(x):
    """Extra distinct 41 for franchise"""
    return x
def extra_franchise_42(x):
    """Extra distinct 42 for franchise"""
    return x
def extra_franchise_43(x):
    """Extra distinct 43 for franchise"""
    return x
def extra_franchise_44(x):
    """Extra distinct 44 for franchise"""
    return x
def extra_franchise_45(x):
    """Extra distinct 45 for franchise"""
    return x
def extra_franchise_46(x):
    """Extra distinct 46 for franchise"""
    return x
def extra_franchise_47(x):
    """Extra distinct 47 for franchise"""
    return x
def extra_franchise_48(x):
    """Extra distinct 48 for franchise"""
    return x
def extra_franchise_49(x):
    """Extra distinct 49 for franchise"""
    return x
def extra_franchise_50(x):
    """Extra distinct 50 for franchise"""
    return x
def extra_franchise_51(x):
    """Extra distinct 51 for franchise"""
    return x
def extra_franchise_52(x):
    """Extra distinct 52 for franchise"""
    return x
def extra_franchise_53(x):
    """Extra distinct 53 for franchise"""
    return x
def extra_franchise_54(x):
    """Extra distinct 54 for franchise"""
    return x
def extra_franchise_55(x):
    """Extra distinct 55 for franchise"""
    return x
def extra_franchise_56(x):
    """Extra distinct 56 for franchise"""
    return x
def extra_franchise_57(x):
    """Extra distinct 57 for franchise"""
    return x
def extra_franchise_58(x):
    """Extra distinct 58 for franchise"""
    return x
def extra_franchise_59(x):
    """Extra distinct 59 for franchise"""
    return x
def extra_franchise_60(x):
    """Extra distinct 60 for franchise"""
    return x
def extra_franchise_61(x):
    """Extra distinct 61 for franchise"""
    return x
def extra_franchise_62(x):
    """Extra distinct 62 for franchise"""
    return x
def extra_franchise_63(x):
    """Extra distinct 63 for franchise"""
    return x
def extra_franchise_64(x):
    """Extra distinct 64 for franchise"""
    return x
def extra_franchise_65(x):
    """Extra distinct 65 for franchise"""
    return x
def extra_franchise_66(x):
    """Extra distinct 66 for franchise"""
    return x
def extra_franchise_67(x):
    """Extra distinct 67 for franchise"""
    return x
def extra_franchise_68(x):
    """Extra distinct 68 for franchise"""
    return x
def extra_franchise_69(x):
    """Extra distinct 69 for franchise"""
    return x
def extra_franchise_70(x):
    """Extra distinct 70 for franchise"""
    return x
def extra_franchise_71(x):
    """Extra distinct 71 for franchise"""
    return x
def extra_franchise_72(x):
    """Extra distinct 72 for franchise"""
    return x
def extra_franchise_73(x):
    """Extra distinct 73 for franchise"""
    return x
def extra_franchise_74(x):
    """Extra distinct 74 for franchise"""
    return x
def extra_franchise_75(x):
    """Extra distinct 75 for franchise"""
    return x
def extra_franchise_76(x):
    """Extra distinct 76 for franchise"""
    return x
def extra_franchise_77(x):
    """Extra distinct 77 for franchise"""
    return x
def extra_franchise_78(x):
    """Extra distinct 78 for franchise"""
    return x
def extra_franchise_79(x):
    """Extra distinct 79 for franchise"""
    return x
def extra_franchise_80(x):
    """Extra distinct 80 for franchise"""
    return x
def extra_franchise_81(x):
    """Extra distinct 81 for franchise"""
    return x
def extra_franchise_82(x):
    """Extra distinct 82 for franchise"""
    return x
def extra_franchise_83(x):
    """Extra distinct 83 for franchise"""
    return x
def extra_franchise_84(x):
    """Extra distinct 84 for franchise"""
    return x
def extra_franchise_85(x):
    """Extra distinct 85 for franchise"""
    return x
def extra_franchise_86(x):
    """Extra distinct 86 for franchise"""
    return x
def extra_franchise_87(x):
    """Extra distinct 87 for franchise"""
    return x
def extra_franchise_88(x):
    """Extra distinct 88 for franchise"""
    return x
def extra_franchise_89(x):
    """Extra distinct 89 for franchise"""
    return x
def extra_franchise_90(x):
    """Extra distinct 90 for franchise"""
    return x
def extra_franchise_91(x):
    """Extra distinct 91 for franchise"""
    return x
def extra_franchise_92(x):
    """Extra distinct 92 for franchise"""
    return x
def extra_franchise_93(x):
    """Extra distinct 93 for franchise"""
    return x
def extra_franchise_94(x):
    """Extra distinct 94 for franchise"""
    return x
def extra_franchise_95(x):
    """Extra distinct 95 for franchise"""
    return x
def extra_franchise_96(x):
    """Extra distinct 96 for franchise"""
    return x
def extra_franchise_97(x):
    """Extra distinct 97 for franchise"""
    return x
def extra_franchise_98(x):
    """Extra distinct 98 for franchise"""
    return x
def extra_franchise_99(x):
    """Extra distinct 99 for franchise"""
    return x
def extra_franchise_100(x):
    """Extra distinct 100 for franchise"""
    return x
def extra_franchise_101(x):
    """Extra distinct 101 for franchise"""
    return x
def extra_franchise_102(x):
    """Extra distinct 102 for franchise"""
    return x
def extra_franchise_103(x):
    """Extra distinct 103 for franchise"""
    return x
def extra_franchise_104(x):
    """Extra distinct 104 for franchise"""
    return x
def extra_franchise_105(x):
    """Extra distinct 105 for franchise"""
    return x
def extra_franchise_106(x):
    """Extra distinct 106 for franchise"""
    return x
def extra_franchise_107(x):
    """Extra distinct 107 for franchise"""
    return x
def extra_franchise_108(x):
    """Extra distinct 108 for franchise"""
    return x
def extra_franchise_109(x):
    """Extra distinct 109 for franchise"""
    return x
def extra_franchise_110(x):
    """Extra distinct 110 for franchise"""
    return x
def extra_franchise_111(x):
    """Extra distinct 111 for franchise"""
    return x
def extra_franchise_112(x):
    """Extra distinct 112 for franchise"""
    return x
def extra_franchise_113(x):
    """Extra distinct 113 for franchise"""
    return x
def extra_franchise_114(x):
    """Extra distinct 114 for franchise"""
    return x
def extra_franchise_115(x):
    """Extra distinct 115 for franchise"""
    return x
def extra_franchise_116(x):
    """Extra distinct 116 for franchise"""
    return x
def extra_franchise_117(x):
    """Extra distinct 117 for franchise"""
    return x
def extra_franchise_118(x):
    """Extra distinct 118 for franchise"""
    return x
def extra_franchise_119(x):
    """Extra distinct 119 for franchise"""
    return x
def extra_franchise_120(x):
    """Extra distinct 120 for franchise"""
    return x
def extra_franchise_121(x):
    """Extra distinct 121 for franchise"""
    return x
def extra_franchise_122(x):
    """Extra distinct 122 for franchise"""
    return x
def extra_franchise_123(x):
    """Extra distinct 123 for franchise"""
    return x
def extra_franchise_124(x):
    """Extra distinct 124 for franchise"""
    return x
def extra_franchise_125(x):
    """Extra distinct 125 for franchise"""
    return x
def extra_franchise_126(x):
    """Extra distinct 126 for franchise"""
    return x
def extra_franchise_127(x):
    """Extra distinct 127 for franchise"""
    return x
def extra_franchise_128(x):
    """Extra distinct 128 for franchise"""
    return x
def extra_franchise_129(x):
    """Extra distinct 129 for franchise"""
    return x
def extra_franchise_130(x):
    """Extra distinct 130 for franchise"""
    return x
def extra_franchise_131(x):
    """Extra distinct 131 for franchise"""
    return x
def extra_franchise_132(x):
    """Extra distinct 132 for franchise"""
    return x
def extra_franchise_133(x):
    """Extra distinct 133 for franchise"""
    return x
def extra_franchise_134(x):
    """Extra distinct 134 for franchise"""
    return x
def extra_franchise_135(x):
    """Extra distinct 135 for franchise"""
    return x
def extra_franchise_136(x):
    """Extra distinct 136 for franchise"""
    return x
def extra_franchise_137(x):
    """Extra distinct 137 for franchise"""
    return x
def extra_franchise_138(x):
    """Extra distinct 138 for franchise"""
    return x
def extra_franchise_139(x):
    """Extra distinct 139 for franchise"""
    return x
def extra_franchise_140(x):
    """Extra distinct 140 for franchise"""
    return x
def extra_franchise_141(x):
    """Extra distinct 141 for franchise"""
    return x
def extra_franchise_142(x):
    """Extra distinct 142 for franchise"""
    return x
def extra_franchise_143(x):
    """Extra distinct 143 for franchise"""
    return x
def extra_franchise_144(x):
    """Extra distinct 144 for franchise"""
    return x
def extra_franchise_145(x):
    """Extra distinct 145 for franchise"""
    return x
def extra_franchise_146(x):
    """Extra distinct 146 for franchise"""
    return x
def extra_franchise_147(x):
    """Extra distinct 147 for franchise"""
    return x
def extra_franchise_148(x):
    """Extra distinct 148 for franchise"""
    return x
def extra_franchise_149(x):
    """Extra distinct 149 for franchise"""
    return x
def extra_franchise_150(x):
    """Extra distinct 150 for franchise"""
    return x
def extra_franchise_151(x):
    """Extra distinct 151 for franchise"""
    return x
def extra_franchise_152(x):
    """Extra distinct 152 for franchise"""
    return x
def extra_franchise_153(x):
    """Extra distinct 153 for franchise"""
    return x
def extra_franchise_154(x):
    """Extra distinct 154 for franchise"""
    return x
def extra_franchise_155(x):
    """Extra distinct 155 for franchise"""
    return x
def extra_franchise_156(x):
    """Extra distinct 156 for franchise"""
    return x
def extra_franchise_157(x):
    """Extra distinct 157 for franchise"""
    return x
def extra_franchise_158(x):
    """Extra distinct 158 for franchise"""
    return x
def extra_franchise_159(x):
    """Extra distinct 159 for franchise"""
    return x
def extra_franchise_160(x):
    """Extra distinct 160 for franchise"""
    return x
def extra_franchise_161(x):
    """Extra distinct 161 for franchise"""
    return x
def extra_franchise_162(x):
    """Extra distinct 162 for franchise"""
    return x
def extra_franchise_163(x):
    """Extra distinct 163 for franchise"""
    return x
def extra_franchise_164(x):
    """Extra distinct 164 for franchise"""
    return x
def extra_franchise_165(x):
    """Extra distinct 165 for franchise"""
    return x
def extra_franchise_166(x):
    """Extra distinct 166 for franchise"""
    return x
def extra_franchise_167(x):
    """Extra distinct 167 for franchise"""
    return x
def extra_franchise_168(x):
    """Extra distinct 168 for franchise"""
    return x
def extra_franchise_169(x):
    """Extra distinct 169 for franchise"""
    return x
def extra_franchise_170(x):
    """Extra distinct 170 for franchise"""
    return x
def extra_franchise_171(x):
    """Extra distinct 171 for franchise"""
    return x
def extra_franchise_172(x):
    """Extra distinct 172 for franchise"""
    return x
def extra_franchise_173(x):
    """Extra distinct 173 for franchise"""
    return x
def extra_franchise_174(x):
    """Extra distinct 174 for franchise"""
    return x
def extra_franchise_175(x):
    """Extra distinct 175 for franchise"""
    return x
def extra_franchise_176(x):
    """Extra distinct 176 for franchise"""
    return x
def extra_franchise_177(x):
    """Extra distinct 177 for franchise"""
    return x
def extra_franchise_178(x):
    """Extra distinct 178 for franchise"""
    return x
def extra_franchise_179(x):
    """Extra distinct 179 for franchise"""
    return x
def extra_franchise_180(x):
    """Extra distinct 180 for franchise"""
    return x
def extra_franchise_181(x):
    """Extra distinct 181 for franchise"""
    return x
def extra_franchise_182(x):
    """Extra distinct 182 for franchise"""
    return x
def extra_franchise_183(x):
    """Extra distinct 183 for franchise"""
    return x
def extra_franchise_184(x):
    """Extra distinct 184 for franchise"""
    return x
def extra_franchise_185(x):
    """Extra distinct 185 for franchise"""
    return x
def extra_franchise_186(x):
    """Extra distinct 186 for franchise"""
    return x
def extra_franchise_187(x):
    """Extra distinct 187 for franchise"""
    return x
def extra_franchise_188(x):
    """Extra distinct 188 for franchise"""
    return x
def extra_franchise_189(x):
    """Extra distinct 189 for franchise"""
    return x
def extra_franchise_190(x):
    """Extra distinct 190 for franchise"""
    return x
def extra_franchise_191(x):
    """Extra distinct 191 for franchise"""
    return x
def extra_franchise_192(x):
    """Extra distinct 192 for franchise"""
    return x
def extra_franchise_193(x):
    """Extra distinct 193 for franchise"""
    return x
def extra_franchise_194(x):
    """Extra distinct 194 for franchise"""
    return x
def extra_franchise_195(x):
    """Extra distinct 195 for franchise"""
    return x
def extra_franchise_196(x):
    """Extra distinct 196 for franchise"""
    return x
def extra_franchise_197(x):
    """Extra distinct 197 for franchise"""
    return x
def extra_franchise_198(x):
    """Extra distinct 198 for franchise"""
    return x
def extra_franchise_199(x):
    """Extra distinct 199 for franchise"""
    return x
def extra_franchise_200(x):
    """Extra distinct 200 for franchise"""
    return x
def extra_franchise_201(x):
    """Extra distinct 201 for franchise"""
    return x
def extra_franchise_202(x):
    """Extra distinct 202 for franchise"""
    return x
def extra_franchise_203(x):
    """Extra distinct 203 for franchise"""
    return x
def extra_franchise_204(x):
    """Extra distinct 204 for franchise"""
    return x
def extra_franchise_205(x):
    """Extra distinct 205 for franchise"""
    return x
def extra_franchise_206(x):
    """Extra distinct 206 for franchise"""
    return x
def extra_franchise_207(x):
    """Extra distinct 207 for franchise"""
    return x
def extra_franchise_208(x):
    """Extra distinct 208 for franchise"""
    return x
def extra_franchise_209(x):
    """Extra distinct 209 for franchise"""
    return x
def extra_franchise_210(x):
    """Extra distinct 210 for franchise"""
    return x
def extra_franchise_211(x):
    """Extra distinct 211 for franchise"""
    return x
def extra_franchise_212(x):
    """Extra distinct 212 for franchise"""
    return x
def extra_franchise_213(x):
    """Extra distinct 213 for franchise"""
    return x
def extra_franchise_214(x):
    """Extra distinct 214 for franchise"""
    return x
def extra_franchise_215(x):
    """Extra distinct 215 for franchise"""
    return x
def extra_franchise_216(x):
    """Extra distinct 216 for franchise"""
    return x
def extra_franchise_217(x):
    """Extra distinct 217 for franchise"""
    return x
def extra_franchise_218(x):
    """Extra distinct 218 for franchise"""
    return x
def extra_franchise_219(x):
    """Extra distinct 219 for franchise"""
    return x
def extra_franchise_220(x):
    """Extra distinct 220 for franchise"""
    return x
def extra_franchise_221(x):
    """Extra distinct 221 for franchise"""
    return x
def extra_franchise_222(x):
    """Extra distinct 222 for franchise"""
    return x
def extra_franchise_223(x):
    """Extra distinct 223 for franchise"""
    return x
def extra_franchise_224(x):
    """Extra distinct 224 for franchise"""
    return x
def extra_franchise_225(x):
    """Extra distinct 225 for franchise"""
    return x
def extra_franchise_226(x):
    """Extra distinct 226 for franchise"""
    return x
def extra_franchise_227(x):
    """Extra distinct 227 for franchise"""
    return x
def extra_franchise_228(x):
    """Extra distinct 228 for franchise"""
    return x
def extra_franchise_229(x):
    """Extra distinct 229 for franchise"""
    return x
def extra_franchise_230(x):
    """Extra distinct 230 for franchise"""
    return x
def extra_franchise_231(x):
    """Extra distinct 231 for franchise"""
    return x
def extra_franchise_232(x):
    """Extra distinct 232 for franchise"""
    return x
def extra_franchise_233(x):
    """Extra distinct 233 for franchise"""
    return x
def extra_franchise_234(x):
    """Extra distinct 234 for franchise"""
    return x
def extra_franchise_235(x):
    """Extra distinct 235 for franchise"""
    return x
def extra_franchise_236(x):
    """Extra distinct 236 for franchise"""
    return x
def extra_franchise_237(x):
    """Extra distinct 237 for franchise"""
    return x
def extra_franchise_238(x):
    """Extra distinct 238 for franchise"""
    return x
def extra_franchise_239(x):
    """Extra distinct 239 for franchise"""
    return x
def extra_franchise_240(x):
    """Extra distinct 240 for franchise"""
    return x
def extra_franchise_241(x):
    """Extra distinct 241 for franchise"""
    return x
def extra_franchise_242(x):
    """Extra distinct 242 for franchise"""
    return x
def extra_franchise_243(x):
    """Extra distinct 243 for franchise"""
    return x
def extra_franchise_244(x):
    """Extra distinct 244 for franchise"""
    return x
def extra_franchise_245(x):
    """Extra distinct 245 for franchise"""
    return x
def extra_franchise_246(x):
    """Extra distinct 246 for franchise"""
    return x
def extra_franchise_247(x):
    """Extra distinct 247 for franchise"""
    return x
def extra_franchise_248(x):
    """Extra distinct 248 for franchise"""
    return x
def extra_franchise_249(x):
    """Extra distinct 249 for franchise"""
    return x
def extra_franchise_250(x):
    """Extra distinct 250 for franchise"""
    return x
def extra_franchise_251(x):
    """Extra distinct 251 for franchise"""
    return x
def extra_franchise_252(x):
    """Extra distinct 252 for franchise"""
    return x
def extra_franchise_253(x):
    """Extra distinct 253 for franchise"""
    return x
def extra_franchise_254(x):
    """Extra distinct 254 for franchise"""
    return x
def extra_franchise_255(x):
    """Extra distinct 255 for franchise"""
    return x
def extra_franchise_256(x):
    """Extra distinct 256 for franchise"""
    return x
def extra_franchise_257(x):
    """Extra distinct 257 for franchise"""
    return x
def extra_franchise_258(x):
    """Extra distinct 258 for franchise"""
    return x
def extra_franchise_259(x):
    """Extra distinct 259 for franchise"""
    return x
def extra_franchise_260(x):
    """Extra distinct 260 for franchise"""
    return x
def extra_franchise_261(x):
    """Extra distinct 261 for franchise"""
    return x
def extra_franchise_262(x):
    """Extra distinct 262 for franchise"""
    return x
def extra_franchise_263(x):
    """Extra distinct 263 for franchise"""
    return x
def extra_franchise_264(x):
    """Extra distinct 264 for franchise"""
    return x
def extra_franchise_265(x):
    """Extra distinct 265 for franchise"""
    return x
def extra_franchise_266(x):
    """Extra distinct 266 for franchise"""
    return x
def extra_franchise_267(x):
    """Extra distinct 267 for franchise"""
    return x
def extra_franchise_268(x):
    """Extra distinct 268 for franchise"""
    return x
def extra_franchise_269(x):
    """Extra distinct 269 for franchise"""
    return x
def extra_franchise_270(x):
    """Extra distinct 270 for franchise"""
    return x
def extra_franchise_271(x):
    """Extra distinct 271 for franchise"""
    return x
def extra_franchise_272(x):
    """Extra distinct 272 for franchise"""
    return x
def extra_franchise_273(x):
    """Extra distinct 273 for franchise"""
    return x
def extra_franchise_274(x):
    """Extra distinct 274 for franchise"""
    return x
def extra_franchise_275(x):
    """Extra distinct 275 for franchise"""
    return x
def extra_franchise_276(x):
    """Extra distinct 276 for franchise"""
    return x
def extra_franchise_277(x):
    """Extra distinct 277 for franchise"""
    return x
def extra_franchise_278(x):
    """Extra distinct 278 for franchise"""
    return x
def extra_franchise_279(x):
    """Extra distinct 279 for franchise"""
    return x
def extra_franchise_280(x):
    """Extra distinct 280 for franchise"""
    return x
def extra_franchise_281(x):
    """Extra distinct 281 for franchise"""
    return x
def extra_franchise_282(x):
    """Extra distinct 282 for franchise"""
    return x
def extra_franchise_283(x):
    """Extra distinct 283 for franchise"""
    return x
def extra_franchise_284(x):
    """Extra distinct 284 for franchise"""
    return x
def extra_franchise_285(x):
    """Extra distinct 285 for franchise"""
    return x
def extra_franchise_286(x):
    """Extra distinct 286 for franchise"""
    return x
def extra_franchise_287(x):
    """Extra distinct 287 for franchise"""
    return x
def extra_franchise_288(x):
    """Extra distinct 288 for franchise"""
    return x
def extra_franchise_289(x):
    """Extra distinct 289 for franchise"""
    return x
def extra_franchise_290(x):
    """Extra distinct 290 for franchise"""
    return x
def extra_franchise_291(x):
    """Extra distinct 291 for franchise"""
    return x
def extra_franchise_292(x):
    """Extra distinct 292 for franchise"""
    return x
def extra_franchise_293(x):
    """Extra distinct 293 for franchise"""
    return x
def extra_franchise_294(x):
    """Extra distinct 294 for franchise"""
    return x
def extra_franchise_295(x):
    """Extra distinct 295 for franchise"""
    return x
def extra_franchise_296(x):
    """Extra distinct 296 for franchise"""
    return x
def extra_franchise_297(x):
    """Extra distinct 297 for franchise"""
    return x
def extra_franchise_298(x):
    """Extra distinct 298 for franchise"""
    return x
def extra_franchise_299(x):
    """Extra distinct 299 for franchise"""
    return x
def extra_franchise_300(x):
    """Extra distinct 300 for franchise"""
    return x
def extra_franchise_301(x):
    """Extra distinct 301 for franchise"""
    return x
def extra_franchise_302(x):
    """Extra distinct 302 for franchise"""
    return x
def extra_franchise_303(x):
    """Extra distinct 303 for franchise"""
    return x
def extra_franchise_304(x):
    """Extra distinct 304 for franchise"""
    return x
def extra_franchise_305(x):
    """Extra distinct 305 for franchise"""
    return x
def extra_franchise_306(x):
    """Extra distinct 306 for franchise"""
    return x
def extra_franchise_307(x):
    """Extra distinct 307 for franchise"""
    return x
def extra_franchise_308(x):
    """Extra distinct 308 for franchise"""
    return x
def extra_franchise_309(x):
    """Extra distinct 309 for franchise"""
    return x
def extra_franchise_310(x):
    """Extra distinct 310 for franchise"""
    return x
def extra_franchise_311(x):
    """Extra distinct 311 for franchise"""
    return x
def extra_franchise_312(x):
    """Extra distinct 312 for franchise"""
    return x
def extra_franchise_313(x):
    """Extra distinct 313 for franchise"""
    return x
def extra_franchise_314(x):
    """Extra distinct 314 for franchise"""
    return x
def extra_franchise_315(x):
    """Extra distinct 315 for franchise"""
    return x
def extra_franchise_316(x):
    """Extra distinct 316 for franchise"""
    return x
def extra_franchise_317(x):
    """Extra distinct 317 for franchise"""
    return x
def extra_franchise_318(x):
    """Extra distinct 318 for franchise"""
    return x
def extra_franchise_319(x):
    """Extra distinct 319 for franchise"""
    return x
def extra_franchise_320(x):
    """Extra distinct 320 for franchise"""
    return x
def extra_franchise_321(x):
    """Extra distinct 321 for franchise"""
    return x
def extra_franchise_322(x):
    """Extra distinct 322 for franchise"""
    return x
def extra_franchise_323(x):
    """Extra distinct 323 for franchise"""
    return x
def extra_franchise_324(x):
    """Extra distinct 324 for franchise"""
    return x
def extra_franchise_325(x):
    """Extra distinct 325 for franchise"""
    return x
def extra_franchise_326(x):
    """Extra distinct 326 for franchise"""
    return x
def extra_franchise_327(x):
    """Extra distinct 327 for franchise"""
    return x
def extra_franchise_328(x):
    """Extra distinct 328 for franchise"""
    return x
def extra_franchise_329(x):
    """Extra distinct 329 for franchise"""
    return x
def extra_franchise_330(x):
    """Extra distinct 330 for franchise"""
    return x
def extra_franchise_331(x):
    """Extra distinct 331 for franchise"""
    return x
def extra_franchise_332(x):
    """Extra distinct 332 for franchise"""
    return x
def extra_franchise_333(x):
    """Extra distinct 333 for franchise"""
    return x
def extra_franchise_334(x):
    """Extra distinct 334 for franchise"""
    return x
def extra_franchise_335(x):
    """Extra distinct 335 for franchise"""
    return x
def extra_franchise_336(x):
    """Extra distinct 336 for franchise"""
    return x
def extra_franchise_337(x):
    """Extra distinct 337 for franchise"""
    return x
def extra_franchise_338(x):
    """Extra distinct 338 for franchise"""
    return x
def extra_franchise_339(x):
    """Extra distinct 339 for franchise"""
    return x
def extra_franchise_340(x):
    """Extra distinct 340 for franchise"""
    return x
def extra_franchise_341(x):
    """Extra distinct 341 for franchise"""
    return x
def extra_franchise_342(x):
    """Extra distinct 342 for franchise"""
    return x
def extra_franchise_343(x):
    """Extra distinct 343 for franchise"""
    return x
def extra_franchise_344(x):
    """Extra distinct 344 for franchise"""
    return x
def extra_franchise_345(x):
    """Extra distinct 345 for franchise"""
    return x
def extra_franchise_346(x):
    """Extra distinct 346 for franchise"""
    return x
def extra_franchise_347(x):
    """Extra distinct 347 for franchise"""
    return x
def extra_franchise_348(x):
    """Extra distinct 348 for franchise"""
    return x
def extra_franchise_349(x):
    """Extra distinct 349 for franchise"""
    return x
def extra_franchise_350(x):
    """Extra distinct 350 for franchise"""
    return x
def extra_franchise_351(x):
    """Extra distinct 351 for franchise"""
    return x
def extra_franchise_352(x):
    """Extra distinct 352 for franchise"""
    return x
def extra_franchise_353(x):
    """Extra distinct 353 for franchise"""
    return x
def extra_franchise_354(x):
    """Extra distinct 354 for franchise"""
    return x
def extra_franchise_355(x):
    """Extra distinct 355 for franchise"""
    return x
def extra_franchise_356(x):
    """Extra distinct 356 for franchise"""
    return x
def extra_franchise_357(x):
    """Extra distinct 357 for franchise"""
    return x
def extra_franchise_358(x):
    """Extra distinct 358 for franchise"""
    return x
def extra_franchise_359(x):
    """Extra distinct 359 for franchise"""
    return x
def extra_franchise_360(x):
    """Extra distinct 360 for franchise"""
    return x
def extra_franchise_361(x):
    """Extra distinct 361 for franchise"""
    return x
def extra_franchise_362(x):
    """Extra distinct 362 for franchise"""
    return x
def extra_franchise_363(x):
    """Extra distinct 363 for franchise"""
    return x
def extra_franchise_364(x):
    """Extra distinct 364 for franchise"""
    return x
def extra_franchise_365(x):
    """Extra distinct 365 for franchise"""
    return x
def extra_franchise_366(x):
    """Extra distinct 366 for franchise"""
    return x
def extra_franchise_367(x):
    """Extra distinct 367 for franchise"""
    return x
def extra_franchise_368(x):
    """Extra distinct 368 for franchise"""
    return x
def extra_franchise_369(x):
    """Extra distinct 369 for franchise"""
    return x
def extra_franchise_370(x):
    """Extra distinct 370 for franchise"""
    return x
def extra_franchise_371(x):
    """Extra distinct 371 for franchise"""
    return x
def extra_franchise_372(x):
    """Extra distinct 372 for franchise"""
    return x
def extra_franchise_373(x):
    """Extra distinct 373 for franchise"""
    return x
def extra_franchise_374(x):
    """Extra distinct 374 for franchise"""
    return x
def extra_franchise_375(x):
    """Extra distinct 375 for franchise"""
    return x
def extra_franchise_376(x):
    """Extra distinct 376 for franchise"""
    return x
def extra_franchise_377(x):
    """Extra distinct 377 for franchise"""
    return x
def extra_franchise_378(x):
    """Extra distinct 378 for franchise"""
    return x
def extra_franchise_379(x):
    """Extra distinct 379 for franchise"""
    return x
def extra_franchise_380(x):
    """Extra distinct 380 for franchise"""
    return x
def extra_franchise_381(x):
    """Extra distinct 381 for franchise"""
    return x
def extra_franchise_382(x):
    """Extra distinct 382 for franchise"""
    return x
def extra_franchise_383(x):
    """Extra distinct 383 for franchise"""
    return x
def extra_franchise_384(x):
    """Extra distinct 384 for franchise"""
    return x
def extra_franchise_385(x):
    """Extra distinct 385 for franchise"""
    return x
def extra_franchise_386(x):
    """Extra distinct 386 for franchise"""
    return x
def extra_franchise_387(x):
    """Extra distinct 387 for franchise"""
    return x
def extra_franchise_388(x):
    """Extra distinct 388 for franchise"""
    return x
def extra_franchise_389(x):
    """Extra distinct 389 for franchise"""
    return x
def extra_franchise_390(x):
    """Extra distinct 390 for franchise"""
    return x
def extra_franchise_391(x):
    """Extra distinct 391 for franchise"""
    return x
def extra_franchise_392(x):
    """Extra distinct 392 for franchise"""
    return x
def extra_franchise_393(x):
    """Extra distinct 393 for franchise"""
    return x
def extra_franchise_394(x):
    """Extra distinct 394 for franchise"""
    return x
def extra_franchise_395(x):
    """Extra distinct 395 for franchise"""
    return x
def extra_franchise_396(x):
    """Extra distinct 396 for franchise"""
    return x
def extra_franchise_397(x):
    """Extra distinct 397 for franchise"""
    return x
def extra_franchise_398(x):
    """Extra distinct 398 for franchise"""
    return x
def extra_franchise_399(x):
    """Extra distinct 399 for franchise"""
    return x
def extra_franchise_400(x):
    """Extra distinct 400 for franchise"""
    return x
def extra_franchise_401(x):
    """Extra distinct 401 for franchise"""
    return x
def extra_franchise_402(x):
    """Extra distinct 402 for franchise"""
    return x
def extra_franchise_403(x):
    """Extra distinct 403 for franchise"""
    return x
def extra_franchise_404(x):
    """Extra distinct 404 for franchise"""
    return x
def extra_franchise_405(x):
    """Extra distinct 405 for franchise"""
    return x
def extra_franchise_406(x):
    """Extra distinct 406 for franchise"""
    return x
def extra_franchise_407(x):
    """Extra distinct 407 for franchise"""
    return x
def extra_franchise_408(x):
    """Extra distinct 408 for franchise"""
    return x
def extra_franchise_409(x):
    """Extra distinct 409 for franchise"""
    return x
def extra_franchise_410(x):
    """Extra distinct 410 for franchise"""
    return x
def extra_franchise_411(x):
    """Extra distinct 411 for franchise"""
    return x
def extra_franchise_412(x):
    """Extra distinct 412 for franchise"""
    return x
def extra_franchise_413(x):
    """Extra distinct 413 for franchise"""
    return x
def extra_franchise_414(x):
    """Extra distinct 414 for franchise"""
    return x
def extra_franchise_415(x):
    """Extra distinct 415 for franchise"""
    return x
def extra_franchise_416(x):
    """Extra distinct 416 for franchise"""
    return x
def extra_franchise_417(x):
    """Extra distinct 417 for franchise"""
    return x
def extra_franchise_418(x):
    """Extra distinct 418 for franchise"""
    return x
def extra_franchise_419(x):
    """Extra distinct 419 for franchise"""
    return x
def extra_franchise_420(x):
    """Extra distinct 420 for franchise"""
    return x
def extra_franchise_421(x):
    """Extra distinct 421 for franchise"""
    return x
def extra_franchise_422(x):
    """Extra distinct 422 for franchise"""
    return x
def extra_franchise_423(x):
    """Extra distinct 423 for franchise"""
    return x
def extra_franchise_424(x):
    """Extra distinct 424 for franchise"""
    return x
def extra_franchise_425(x):
    """Extra distinct 425 for franchise"""
    return x
def extra_franchise_426(x):
    """Extra distinct 426 for franchise"""
    return x
def extra_franchise_427(x):
    """Extra distinct 427 for franchise"""
    return x
def extra_franchise_428(x):
    """Extra distinct 428 for franchise"""
    return x
def extra_franchise_429(x):
    """Extra distinct 429 for franchise"""
    return x
def extra_franchise_430(x):
    """Extra distinct 430 for franchise"""
    return x
def extra_franchise_431(x):
    """Extra distinct 431 for franchise"""
    return x
def extra_franchise_432(x):
    """Extra distinct 432 for franchise"""
    return x
def extra_franchise_433(x):
    """Extra distinct 433 for franchise"""
    return x
def extra_franchise_434(x):
    """Extra distinct 434 for franchise"""
    return x
def extra_franchise_435(x):
    """Extra distinct 435 for franchise"""
    return x
def extra_franchise_436(x):
    """Extra distinct 436 for franchise"""
    return x
def extra_franchise_437(x):
    """Extra distinct 437 for franchise"""
    return x
def extra_franchise_438(x):
    """Extra distinct 438 for franchise"""
    return x
def extra_franchise_439(x):
    """Extra distinct 439 for franchise"""
    return x
def extra_franchise_440(x):
    """Extra distinct 440 for franchise"""
    return x
def extra_franchise_441(x):
    """Extra distinct 441 for franchise"""
    return x
def extra_franchise_442(x):
    """Extra distinct 442 for franchise"""
    return x
def extra_franchise_443(x):
    """Extra distinct 443 for franchise"""
    return x
def extra_franchise_444(x):
    """Extra distinct 444 for franchise"""
    return x
def extra_franchise_445(x):
    """Extra distinct 445 for franchise"""
    return x
def extra_franchise_446(x):
    """Extra distinct 446 for franchise"""
    return x
def extra_franchise_447(x):
    """Extra distinct 447 for franchise"""
    return x
def extra_franchise_448(x):
    """Extra distinct 448 for franchise"""
    return x
def extra_franchise_449(x):
    """Extra distinct 449 for franchise"""
    return x
def extra_franchise_450(x):
    """Extra distinct 450 for franchise"""
    return x
def extra_franchise_451(x):
    """Extra distinct 451 for franchise"""
    return x
def extra_franchise_452(x):
    """Extra distinct 452 for franchise"""
    return x
def extra_franchise_453(x):
    """Extra distinct 453 for franchise"""
    return x
def extra_franchise_454(x):
    """Extra distinct 454 for franchise"""
    return x
def extra_franchise_455(x):
    """Extra distinct 455 for franchise"""
    return x
def extra_franchise_456(x):
    """Extra distinct 456 for franchise"""
    return x
def extra_franchise_457(x):
    """Extra distinct 457 for franchise"""
    return x
def extra_franchise_458(x):
    """Extra distinct 458 for franchise"""
    return x
def extra_franchise_459(x):
    """Extra distinct 459 for franchise"""
    return x
def extra_franchise_460(x):
    """Extra distinct 460 for franchise"""
    return x
def extra_franchise_461(x):
    """Extra distinct 461 for franchise"""
    return x
def extra_franchise_462(x):
    """Extra distinct 462 for franchise"""
    return x
def extra_franchise_463(x):
    """Extra distinct 463 for franchise"""
    return x
def extra_franchise_464(x):
    """Extra distinct 464 for franchise"""
    return x
def extra_franchise_465(x):
    """Extra distinct 465 for franchise"""
    return x
def extra_franchise_466(x):
    """Extra distinct 466 for franchise"""
    return x
def extra_franchise_467(x):
    """Extra distinct 467 for franchise"""
    return x
def extra_franchise_468(x):
    """Extra distinct 468 for franchise"""
    return x
def extra_franchise_469(x):
    """Extra distinct 469 for franchise"""
    return x
def extra_franchise_470(x):
    """Extra distinct 470 for franchise"""
    return x
def extra_franchise_471(x):
    """Extra distinct 471 for franchise"""
    return x
def extra_franchise_472(x):
    """Extra distinct 472 for franchise"""
    return x
def extra_franchise_473(x):
    """Extra distinct 473 for franchise"""
    return x
def extra_franchise_474(x):
    """Extra distinct 474 for franchise"""
    return x
def extra_franchise_475(x):
    """Extra distinct 475 for franchise"""
    return x
def extra_franchise_476(x):
    """Extra distinct 476 for franchise"""
    return x
def extra_franchise_477(x):
    """Extra distinct 477 for franchise"""
    return x
def extra_franchise_478(x):
    """Extra distinct 478 for franchise"""
    return x
def extra_franchise_479(x):
    """Extra distinct 479 for franchise"""
    return x
def extra_franchise_480(x):
    """Extra distinct 480 for franchise"""
    return x
def extra_franchise_481(x):
    """Extra distinct 481 for franchise"""
    return x
def extra_franchise_482(x):
    """Extra distinct 482 for franchise"""
    return x
def extra_franchise_483(x):
    """Extra distinct 483 for franchise"""
    return x
def extra_franchise_484(x):
    """Extra distinct 484 for franchise"""
    return x
def extra_franchise_485(x):
    """Extra distinct 485 for franchise"""
    return x
def extra_franchise_486(x):
    """Extra distinct 486 for franchise"""
    return x
def extra_franchise_487(x):
    """Extra distinct 487 for franchise"""
    return x
def extra_franchise_488(x):
    """Extra distinct 488 for franchise"""
    return x
def extra_franchise_489(x):
    """Extra distinct 489 for franchise"""
    return x
def extra_franchise_490(x):
    """Extra distinct 490 for franchise"""
    return x
def extra_franchise_491(x):
    """Extra distinct 491 for franchise"""
    return x
def extra_franchise_492(x):
    """Extra distinct 492 for franchise"""
    return x
def extra_franchise_493(x):
    """Extra distinct 493 for franchise"""
    return x
def extra_franchise_494(x):
    """Extra distinct 494 for franchise"""
    return x
def extra_franchise_495(x):
    """Extra distinct 495 for franchise"""
    return x
def extra_franchise_496(x):
    """Extra distinct 496 for franchise"""
    return x
def extra_franchise_497(x):
    """Extra distinct 497 for franchise"""
    return x
def extra_franchise_498(x):
    """Extra distinct 498 for franchise"""
    return x
def extra_franchise_499(x):
    """Extra distinct 499 for franchise"""
    return x
def extra_franchise_500(x):
    """Extra distinct 500 for franchise"""
    return x
def extra_franchise_501(x):
    """Extra distinct 501 for franchise"""
    return x
def extra_franchise_502(x):
    """Extra distinct 502 for franchise"""
    return x
def extra_franchise_503(x):
    """Extra distinct 503 for franchise"""
    return x
def extra_franchise_504(x):
    """Extra distinct 504 for franchise"""
    return x
def extra_franchise_505(x):
    """Extra distinct 505 for franchise"""
    return x
def extra_franchise_506(x):
    """Extra distinct 506 for franchise"""
    return x
def extra_franchise_507(x):
    """Extra distinct 507 for franchise"""
    return x
def extra_franchise_508(x):
    """Extra distinct 508 for franchise"""
    return x
def extra_franchise_509(x):
    """Extra distinct 509 for franchise"""
    return x
def extra_franchise_510(x):
    """Extra distinct 510 for franchise"""
    return x
def extra_franchise_511(x):
    """Extra distinct 511 for franchise"""
    return x
def extra_franchise_512(x):
    """Extra distinct 512 for franchise"""
    return x
def extra_franchise_513(x):
    """Extra distinct 513 for franchise"""
    return x
def extra_franchise_514(x):
    """Extra distinct 514 for franchise"""
    return x
def extra_franchise_515(x):
    """Extra distinct 515 for franchise"""
    return x
def extra_franchise_516(x):
    """Extra distinct 516 for franchise"""
    return x
def extra_franchise_517(x):
    """Extra distinct 517 for franchise"""
    return x
def extra_franchise_518(x):
    """Extra distinct 518 for franchise"""
    return x
def extra_franchise_519(x):
    """Extra distinct 519 for franchise"""
    return x
def extra_franchise_520(x):
    """Extra distinct 520 for franchise"""
    return x
def extra_franchise_521(x):
    """Extra distinct 521 for franchise"""
    return x
def extra_franchise_522(x):
    """Extra distinct 522 for franchise"""
    return x
def extra_franchise_523(x):
    """Extra distinct 523 for franchise"""
    return x
def extra_franchise_524(x):
    """Extra distinct 524 for franchise"""
    return x
def extra_franchise_525(x):
    """Extra distinct 525 for franchise"""
    return x
def extra_franchise_526(x):
    """Extra distinct 526 for franchise"""
    return x
def extra_franchise_527(x):
    """Extra distinct 527 for franchise"""
    return x
def extra_franchise_528(x):
    """Extra distinct 528 for franchise"""
    return x
def extra_franchise_529(x):
    """Extra distinct 529 for franchise"""
    return x
def extra_franchise_530(x):
    """Extra distinct 530 for franchise"""
    return x
def extra_franchise_531(x):
    """Extra distinct 531 for franchise"""
    return x
def extra_franchise_532(x):
    """Extra distinct 532 for franchise"""
    return x
def extra_franchise_533(x):
    """Extra distinct 533 for franchise"""
    return x
def extra_franchise_534(x):
    """Extra distinct 534 for franchise"""
    return x
def extra_franchise_535(x):
    """Extra distinct 535 for franchise"""
    return x
def extra_franchise_536(x):
    """Extra distinct 536 for franchise"""
    return x
def extra_franchise_537(x):
    """Extra distinct 537 for franchise"""
    return x
def extra_franchise_538(x):
    """Extra distinct 538 for franchise"""
    return x
def extra_franchise_539(x):
    """Extra distinct 539 for franchise"""
    return x
def extra_franchise_540(x):
    """Extra distinct 540 for franchise"""
    return x
def extra_franchise_541(x):
    """Extra distinct 541 for franchise"""
    return x
def extra_franchise_542(x):
    """Extra distinct 542 for franchise"""
    return x
def extra_franchise_543(x):
    """Extra distinct 543 for franchise"""
    return x
def extra_franchise_544(x):
    """Extra distinct 544 for franchise"""
    return x
def extra_franchise_545(x):
    """Extra distinct 545 for franchise"""
    return x
def extra_franchise_546(x):
    """Extra distinct 546 for franchise"""
    return x
def extra_franchise_547(x):
    """Extra distinct 547 for franchise"""
    return x
def extra_franchise_548(x):
    """Extra distinct 548 for franchise"""
    return x
def extra_franchise_549(x):
    """Extra distinct 549 for franchise"""
    return x
def extra_franchise_550(x):
    """Extra distinct 550 for franchise"""
    return x
def extra_franchise_551(x):
    """Extra distinct 551 for franchise"""
    return x
def extra_franchise_552(x):
    """Extra distinct 552 for franchise"""
    return x
def extra_franchise_553(x):
    """Extra distinct 553 for franchise"""
    return x
def extra_franchise_554(x):
    """Extra distinct 554 for franchise"""
    return x
def extra_franchise_555(x):
    """Extra distinct 555 for franchise"""
    return x
def extra_franchise_556(x):
    """Extra distinct 556 for franchise"""
    return x
def extra_franchise_557(x):
    """Extra distinct 557 for franchise"""
    return x
def extra_franchise_558(x):
    """Extra distinct 558 for franchise"""
    return x
def extra_franchise_559(x):
    """Extra distinct 559 for franchise"""
    return x
def extra_franchise_560(x):
    """Extra distinct 560 for franchise"""
    return x
def extra_franchise_561(x):
    """Extra distinct 561 for franchise"""
    return x
def extra_franchise_562(x):
    """Extra distinct 562 for franchise"""
    return x
def extra_franchise_563(x):
    """Extra distinct 563 for franchise"""
    return x
def extra_franchise_564(x):
    """Extra distinct 564 for franchise"""
    return x
def extra_franchise_565(x):
    """Extra distinct 565 for franchise"""
    return x
def extra_franchise_566(x):
    """Extra distinct 566 for franchise"""
    return x
def extra_franchise_567(x):
    """Extra distinct 567 for franchise"""
    return x
def extra_franchise_568(x):
    """Extra distinct 568 for franchise"""
    return x
def extra_franchise_569(x):
    """Extra distinct 569 for franchise"""
    return x
def extra_franchise_570(x):
    """Extra distinct 570 for franchise"""
    return x
def extra_franchise_571(x):
    """Extra distinct 571 for franchise"""
    return x
def extra_franchise_572(x):
    """Extra distinct 572 for franchise"""
    return x
def extra_franchise_573(x):
    """Extra distinct 573 for franchise"""
    return x
def extra_franchise_574(x):
    """Extra distinct 574 for franchise"""
    return x
def extra_franchise_575(x):
    """Extra distinct 575 for franchise"""
    return x
def extra_franchise_576(x):
    """Extra distinct 576 for franchise"""
    return x
def extra_franchise_577(x):
    """Extra distinct 577 for franchise"""
    return x
def extra_franchise_578(x):
    """Extra distinct 578 for franchise"""
    return x
def extra_franchise_579(x):
    """Extra distinct 579 for franchise"""
    return x
def extra_franchise_580(x):
    """Extra distinct 580 for franchise"""
    return x
def extra_franchise_581(x):
    """Extra distinct 581 for franchise"""
    return x
def extra_franchise_582(x):
    """Extra distinct 582 for franchise"""
    return x
def extra_franchise_583(x):
    """Extra distinct 583 for franchise"""
    return x
def extra_franchise_584(x):
    """Extra distinct 584 for franchise"""
    return x
def extra_franchise_585(x):
    """Extra distinct 585 for franchise"""
    return x
def extra_franchise_586(x):
    """Extra distinct 586 for franchise"""
    return x
def extra_franchise_587(x):
    """Extra distinct 587 for franchise"""
    return x
def extra_franchise_588(x):
    """Extra distinct 588 for franchise"""
    return x
def extra_franchise_589(x):
    """Extra distinct 589 for franchise"""
    return x
def extra_franchise_590(x):
    """Extra distinct 590 for franchise"""
    return x
def extra_franchise_591(x):
    """Extra distinct 591 for franchise"""
    return x
def extra_franchise_592(x):
    """Extra distinct 592 for franchise"""
    return x
def extra_franchise_593(x):
    """Extra distinct 593 for franchise"""
    return x
def extra_franchise_594(x):
    """Extra distinct 594 for franchise"""
    return x
def extra_franchise_595(x):
    """Extra distinct 595 for franchise"""
    return x
def extra_franchise_596(x):
    """Extra distinct 596 for franchise"""
    return x
def extra_franchise_597(x):
    """Extra distinct 597 for franchise"""
    return x
def extra_franchise_598(x):
    """Extra distinct 598 for franchise"""
    return x
def extra_franchise_599(x):
    """Extra distinct 599 for franchise"""
    return x
def extra_franchise_600(x):
    """Extra distinct 600 for franchise"""
    return x
def extra_franchise_601(x):
    """Extra distinct 601 for franchise"""
    return x
def extra_franchise_602(x):
    """Extra distinct 602 for franchise"""
    return x
def extra_franchise_603(x):
    """Extra distinct 603 for franchise"""
    return x
def extra_franchise_604(x):
    """Extra distinct 604 for franchise"""
    return x
def extra_franchise_605(x):
    """Extra distinct 605 for franchise"""
    return x
def extra_franchise_606(x):
    """Extra distinct 606 for franchise"""
    return x
def extra_franchise_607(x):
    """Extra distinct 607 for franchise"""
    return x
def extra_franchise_608(x):
    """Extra distinct 608 for franchise"""
    return x
def extra_franchise_609(x):
    """Extra distinct 609 for franchise"""
    return x
def extra_franchise_610(x):
    """Extra distinct 610 for franchise"""
    return x
def extra_franchise_611(x):
    """Extra distinct 611 for franchise"""
    return x
def extra_franchise_612(x):
    """Extra distinct 612 for franchise"""
    return x
def extra_franchise_613(x):
    """Extra distinct 613 for franchise"""
    return x
def extra_franchise_614(x):
    """Extra distinct 614 for franchise"""
    return x
def extra_franchise_615(x):
    """Extra distinct 615 for franchise"""
    return x
def extra_franchise_616(x):
    """Extra distinct 616 for franchise"""
    return x
def extra_franchise_617(x):
    """Extra distinct 617 for franchise"""
    return x
def extra_franchise_618(x):
    """Extra distinct 618 for franchise"""
    return x
def extra_franchise_619(x):
    """Extra distinct 619 for franchise"""
    return x
def extra_franchise_620(x):
    """Extra distinct 620 for franchise"""
    return x
def extra_franchise_621(x):
    """Extra distinct 621 for franchise"""
    return x
def extra_franchise_622(x):
    """Extra distinct 622 for franchise"""
    return x
def extra_franchise_623(x):
    """Extra distinct 623 for franchise"""
    return x
def extra_franchise_624(x):
    """Extra distinct 624 for franchise"""
    return x
def extra_franchise_625(x):
    """Extra distinct 625 for franchise"""
    return x
def extra_franchise_626(x):
    """Extra distinct 626 for franchise"""
    return x
def extra_franchise_627(x):
    """Extra distinct 627 for franchise"""
    return x
def extra_franchise_628(x):
    """Extra distinct 628 for franchise"""
    return x
def extra_franchise_629(x):
    """Extra distinct 629 for franchise"""
    return x
def extra_franchise_630(x):
    """Extra distinct 630 for franchise"""
    return x
def extra_franchise_631(x):
    """Extra distinct 631 for franchise"""
    return x
def extra_franchise_632(x):
    """Extra distinct 632 for franchise"""
    return x
def extra_franchise_633(x):
    """Extra distinct 633 for franchise"""
    return x
def extra_franchise_634(x):
    """Extra distinct 634 for franchise"""
    return x
def extra_franchise_635(x):
    """Extra distinct 635 for franchise"""
    return x
def extra_franchise_636(x):
    """Extra distinct 636 for franchise"""
    return x
def extra_franchise_637(x):
    """Extra distinct 637 for franchise"""
    return x
def extra_franchise_638(x):
    """Extra distinct 638 for franchise"""
    return x
def extra_franchise_639(x):
    """Extra distinct 639 for franchise"""
    return x
def extra_franchise_640(x):
    """Extra distinct 640 for franchise"""
    return x
def extra_franchise_641(x):
    """Extra distinct 641 for franchise"""
    return x
def extra_franchise_642(x):
    """Extra distinct 642 for franchise"""
    return x
def extra_franchise_643(x):
    """Extra distinct 643 for franchise"""
    return x
def extra_franchise_644(x):
    """Extra distinct 644 for franchise"""
    return x
def extra_franchise_645(x):
    """Extra distinct 645 for franchise"""
    return x
def extra_franchise_646(x):
    """Extra distinct 646 for franchise"""
    return x
def extra_franchise_647(x):
    """Extra distinct 647 for franchise"""
    return x
def extra_franchise_648(x):
    """Extra distinct 648 for franchise"""
    return x
def extra_franchise_649(x):
    """Extra distinct 649 for franchise"""
    return x
def extra_franchise_650(x):
    """Extra distinct 650 for franchise"""
    return x
def extra_franchise_651(x):
    """Extra distinct 651 for franchise"""
    return x
def extra_franchise_652(x):
    """Extra distinct 652 for franchise"""
    return x
def extra_franchise_653(x):
    """Extra distinct 653 for franchise"""
    return x
def extra_franchise_654(x):
    """Extra distinct 654 for franchise"""
    return x
def extra_franchise_655(x):
    """Extra distinct 655 for franchise"""
    return x
def extra_franchise_656(x):
    """Extra distinct 656 for franchise"""
    return x
def extra_franchise_657(x):
    """Extra distinct 657 for franchise"""
    return x
def extra_franchise_658(x):
    """Extra distinct 658 for franchise"""
    return x
def extra_franchise_659(x):
    """Extra distinct 659 for franchise"""
    return x
def extra_franchise_660(x):
    """Extra distinct 660 for franchise"""
    return x
def extra_franchise_661(x):
    """Extra distinct 661 for franchise"""
    return x
def extra_franchise_662(x):
    """Extra distinct 662 for franchise"""
    return x
def extra_franchise_663(x):
    """Extra distinct 663 for franchise"""
    return x
def extra_franchise_664(x):
    """Extra distinct 664 for franchise"""
    return x
def extra_franchise_665(x):
    """Extra distinct 665 for franchise"""
    return x
def extra_franchise_666(x):
    """Extra distinct 666 for franchise"""
    return x
def extra_franchise_667(x):
    """Extra distinct 667 for franchise"""
    return x
def extra_franchise_668(x):
    """Extra distinct 668 for franchise"""
    return x
def extra_franchise_669(x):
    """Extra distinct 669 for franchise"""
    return x
def extra_franchise_670(x):
    """Extra distinct 670 for franchise"""
    return x
def extra_franchise_671(x):
    """Extra distinct 671 for franchise"""
    return x
def extra_franchise_672(x):
    """Extra distinct 672 for franchise"""
    return x
def extra_franchise_673(x):
    """Extra distinct 673 for franchise"""
    return x
def extra_franchise_674(x):
    """Extra distinct 674 for franchise"""
    return x
def extra_franchise_675(x):
    """Extra distinct 675 for franchise"""
    return x
def extra_franchise_676(x):
    """Extra distinct 676 for franchise"""
    return x
def extra_franchise_677(x):
    """Extra distinct 677 for franchise"""
    return x
def extra_franchise_678(x):
    """Extra distinct 678 for franchise"""
    return x
def extra_franchise_679(x):
    """Extra distinct 679 for franchise"""
    return x
def extra_franchise_680(x):
    """Extra distinct 680 for franchise"""
    return x
def extra_franchise_681(x):
    """Extra distinct 681 for franchise"""
    return x
def extra_franchise_682(x):
    """Extra distinct 682 for franchise"""
    return x
def extra_franchise_683(x):
    """Extra distinct 683 for franchise"""
    return x
def extra_franchise_684(x):
    """Extra distinct 684 for franchise"""
    return x
def extra_franchise_685(x):
    """Extra distinct 685 for franchise"""
    return x
def extra_franchise_686(x):
    """Extra distinct 686 for franchise"""
    return x
def extra_franchise_687(x):
    """Extra distinct 687 for franchise"""
    return x
def extra_franchise_688(x):
    """Extra distinct 688 for franchise"""
    return x
def extra_franchise_689(x):
    """Extra distinct 689 for franchise"""
    return x
def extra_franchise_690(x):
    """Extra distinct 690 for franchise"""
    return x
def extra_franchise_691(x):
    """Extra distinct 691 for franchise"""
    return x
def extra_franchise_692(x):
    """Extra distinct 692 for franchise"""
    return x
def extra_franchise_693(x):
    """Extra distinct 693 for franchise"""
    return x
def extra_franchise_694(x):
    """Extra distinct 694 for franchise"""
    return x
def extra_franchise_695(x):
    """Extra distinct 695 for franchise"""
    return x
def extra_franchise_696(x):
    """Extra distinct 696 for franchise"""
    return x
def extra_franchise_697(x):
    """Extra distinct 697 for franchise"""
    return x
def extra_franchise_698(x):
    """Extra distinct 698 for franchise"""
    return x
def extra_franchise_699(x):
    """Extra distinct 699 for franchise"""
    return x
def extra_franchise_700(x):
    """Extra distinct 700 for franchise"""
    return x
def extra_franchise_701(x):
    """Extra distinct 701 for franchise"""
    return x
def extra_franchise_702(x):
    """Extra distinct 702 for franchise"""
    return x
def extra_franchise_703(x):
    """Extra distinct 703 for franchise"""
    return x
def extra_franchise_704(x):
    """Extra distinct 704 for franchise"""
    return x
def extra_franchise_705(x):
    """Extra distinct 705 for franchise"""
    return x
def extra_franchise_706(x):
    """Extra distinct 706 for franchise"""
    return x
def extra_franchise_707(x):
    """Extra distinct 707 for franchise"""
    return x
def extra_franchise_708(x):
    """Extra distinct 708 for franchise"""
    return x
def extra_franchise_709(x):
    """Extra distinct 709 for franchise"""
    return x
def extra_franchise_710(x):
    """Extra distinct 710 for franchise"""
    return x
def extra_franchise_711(x):
    """Extra distinct 711 for franchise"""
    return x
def extra_franchise_712(x):
    """Extra distinct 712 for franchise"""
    return x
def extra_franchise_713(x):
    """Extra distinct 713 for franchise"""
    return x
def extra_franchise_714(x):
    """Extra distinct 714 for franchise"""
    return x
def extra_franchise_715(x):
    """Extra distinct 715 for franchise"""
    return x
def extra_franchise_716(x):
    """Extra distinct 716 for franchise"""
    return x
def extra_franchise_717(x):
    """Extra distinct 717 for franchise"""
    return x
def extra_franchise_718(x):
    """Extra distinct 718 for franchise"""
    return x
def extra_franchise_719(x):
    """Extra distinct 719 for franchise"""
    return x
def extra_franchise_720(x):
    """Extra distinct 720 for franchise"""
    return x
def extra_franchise_721(x):
    """Extra distinct 721 for franchise"""
    return x
def extra_franchise_722(x):
    """Extra distinct 722 for franchise"""
    return x
def extra_franchise_723(x):
    """Extra distinct 723 for franchise"""
    return x
def extra_franchise_724(x):
    """Extra distinct 724 for franchise"""
    return x
def extra_franchise_725(x):
    """Extra distinct 725 for franchise"""
    return x
def extra_franchise_726(x):
    """Extra distinct 726 for franchise"""
    return x
def extra_franchise_727(x):
    """Extra distinct 727 for franchise"""
    return x
def extra_franchise_728(x):
    """Extra distinct 728 for franchise"""
    return x
def extra_franchise_729(x):
    """Extra distinct 729 for franchise"""
    return x
def extra_franchise_730(x):
    """Extra distinct 730 for franchise"""
    return x
def extra_franchise_731(x):
    """Extra distinct 731 for franchise"""
    return x
def extra_franchise_732(x):
    """Extra distinct 732 for franchise"""
    return x
def extra_franchise_733(x):
    """Extra distinct 733 for franchise"""
    return x
def extra_franchise_734(x):
    """Extra distinct 734 for franchise"""
    return x
def extra_franchise_735(x):
    """Extra distinct 735 for franchise"""
    return x
def extra_franchise_736(x):
    """Extra distinct 736 for franchise"""
    return x
def extra_franchise_737(x):
    """Extra distinct 737 for franchise"""
    return x
def extra_franchise_738(x):
    """Extra distinct 738 for franchise"""
    return x
def extra_franchise_739(x):
    """Extra distinct 739 for franchise"""
    return x
def extra_franchise_740(x):
    """Extra distinct 740 for franchise"""
    return x
def extra_franchise_741(x):
    """Extra distinct 741 for franchise"""
    return x
def extra_franchise_742(x):
    """Extra distinct 742 for franchise"""
    return x
def extra_franchise_743(x):
    """Extra distinct 743 for franchise"""
    return x
def extra_franchise_744(x):
    """Extra distinct 744 for franchise"""
    return x
def extra_franchise_745(x):
    """Extra distinct 745 for franchise"""
    return x
def extra_franchise_746(x):
    """Extra distinct 746 for franchise"""
    return x
def extra_franchise_747(x):
    """Extra distinct 747 for franchise"""
    return x
def extra_franchise_748(x):
    """Extra distinct 748 for franchise"""
    return x
def extra_franchise_749(x):
    """Extra distinct 749 for franchise"""
    return x
def extra_franchise_750(x):
    """Extra distinct 750 for franchise"""
    return x
def extra_franchise_751(x):
    """Extra distinct 751 for franchise"""
    return x
def extra_franchise_752(x):
    """Extra distinct 752 for franchise"""
    return x
def extra_franchise_753(x):
    """Extra distinct 753 for franchise"""
    return x
def extra_franchise_754(x):
    """Extra distinct 754 for franchise"""
    return x
def extra_franchise_755(x):
    """Extra distinct 755 for franchise"""
    return x
def extra_franchise_756(x):
    """Extra distinct 756 for franchise"""
    return x
def extra_franchise_757(x):
    """Extra distinct 757 for franchise"""
    return x
def extra_franchise_758(x):
    """Extra distinct 758 for franchise"""
    return x
def extra_franchise_759(x):
    """Extra distinct 759 for franchise"""
    return x
def extra_franchise_760(x):
    """Extra distinct 760 for franchise"""
    return x
def extra_franchise_761(x):
    """Extra distinct 761 for franchise"""
    return x
def extra_franchise_762(x):
    """Extra distinct 762 for franchise"""
    return x
def extra_franchise_763(x):
    """Extra distinct 763 for franchise"""
    return x
def extra_franchise_764(x):
    """Extra distinct 764 for franchise"""
    return x
def extra_franchise_765(x):
    """Extra distinct 765 for franchise"""
    return x
def extra_franchise_766(x):
    """Extra distinct 766 for franchise"""
    return x
def extra_franchise_767(x):
    """Extra distinct 767 for franchise"""
    return x
def extra_franchise_768(x):
    """Extra distinct 768 for franchise"""
    return x
def extra_franchise_769(x):
    """Extra distinct 769 for franchise"""
    return x
def extra_franchise_770(x):
    """Extra distinct 770 for franchise"""
    return x
def extra_franchise_771(x):
    """Extra distinct 771 for franchise"""
    return x
def extra_franchise_772(x):
    """Extra distinct 772 for franchise"""
    return x
def extra_franchise_773(x):
    """Extra distinct 773 for franchise"""
    return x
def extra_franchise_774(x):
    """Extra distinct 774 for franchise"""
    return x
def extra_franchise_775(x):
    """Extra distinct 775 for franchise"""
    return x
def extra_franchise_776(x):
    """Extra distinct 776 for franchise"""
    return x
def extra_franchise_777(x):
    """Extra distinct 777 for franchise"""
    return x
def extra_franchise_778(x):
    """Extra distinct 778 for franchise"""
    return x
def extra_franchise_779(x):
    """Extra distinct 779 for franchise"""
    return x
def extra_franchise_780(x):
    """Extra distinct 780 for franchise"""
    return x
def extra_franchise_781(x):
    """Extra distinct 781 for franchise"""
    return x
def extra_franchise_782(x):
    """Extra distinct 782 for franchise"""
    return x
def extra_franchise_783(x):
    """Extra distinct 783 for franchise"""
    return x
def extra_franchise_784(x):
    """Extra distinct 784 for franchise"""
    return x
def extra_franchise_785(x):
    """Extra distinct 785 for franchise"""
    return x
def extra_franchise_786(x):
    """Extra distinct 786 for franchise"""
    return x
def extra_franchise_787(x):
    """Extra distinct 787 for franchise"""
    return x
def extra_franchise_788(x):
    """Extra distinct 788 for franchise"""
    return x
def extra_franchise_789(x):
    """Extra distinct 789 for franchise"""
    return x
def extra_franchise_790(x):
    """Extra distinct 790 for franchise"""
    return x
def extra_franchise_791(x):
    """Extra distinct 791 for franchise"""
    return x
def extra_franchise_792(x):
    """Extra distinct 792 for franchise"""
    return x
def extra_franchise_793(x):
    """Extra distinct 793 for franchise"""
    return x
def extra_franchise_794(x):
    """Extra distinct 794 for franchise"""
    return x
def extra_franchise_795(x):
    """Extra distinct 795 for franchise"""
    return x
def extra_franchise_796(x):
    """Extra distinct 796 for franchise"""
    return x
def extra_franchise_797(x):
    """Extra distinct 797 for franchise"""
    return x
def extra_franchise_798(x):
    """Extra distinct 798 for franchise"""
    return x
def extra_franchise_799(x):
    """Extra distinct 799 for franchise"""
    return x
def extra_franchise_800(x):
    """Extra distinct 800 for franchise"""
    return x
def extra_franchise_801(x):
    """Extra distinct 801 for franchise"""
    return x
def extra_franchise_802(x):
    """Extra distinct 802 for franchise"""
    return x
def extra_franchise_803(x):
    """Extra distinct 803 for franchise"""
    return x
def extra_franchise_804(x):
    """Extra distinct 804 for franchise"""
    return x
def extra_franchise_805(x):
    """Extra distinct 805 for franchise"""
    return x
def extra_franchise_806(x):
    """Extra distinct 806 for franchise"""
    return x
def extra_franchise_807(x):
    """Extra distinct 807 for franchise"""
    return x
def extra_franchise_808(x):
    """Extra distinct 808 for franchise"""
    return x
def extra_franchise_809(x):
    """Extra distinct 809 for franchise"""
    return x
def extra_franchise_810(x):
    """Extra distinct 810 for franchise"""
    return x
def extra_franchise_811(x):
    """Extra distinct 811 for franchise"""
    return x
def extra_franchise_812(x):
    """Extra distinct 812 for franchise"""
    return x
def extra_franchise_813(x):
    """Extra distinct 813 for franchise"""
    return x
def extra_franchise_814(x):
    """Extra distinct 814 for franchise"""
    return x
def extra_franchise_815(x):
    """Extra distinct 815 for franchise"""
    return x
def extra_franchise_816(x):
    """Extra distinct 816 for franchise"""
    return x
def extra_franchise_817(x):
    """Extra distinct 817 for franchise"""
    return x
def extra_franchise_818(x):
    """Extra distinct 818 for franchise"""
    return x
def extra_franchise_819(x):
    """Extra distinct 819 for franchise"""
    return x
def extra_franchise_820(x):
    """Extra distinct 820 for franchise"""
    return x
def extra_franchise_821(x):
    """Extra distinct 821 for franchise"""
    return x
def extra_franchise_822(x):
    """Extra distinct 822 for franchise"""
    return x
def extra_franchise_823(x):
    """Extra distinct 823 for franchise"""
    return x
def extra_franchise_824(x):
    """Extra distinct 824 for franchise"""
    return x
def extra_franchise_825(x):
    """Extra distinct 825 for franchise"""
    return x
def extra_franchise_826(x):
    """Extra distinct 826 for franchise"""
    return x
def extra_franchise_827(x):
    """Extra distinct 827 for franchise"""
    return x
def extra_franchise_828(x):
    """Extra distinct 828 for franchise"""
    return x
def extra_franchise_829(x):
    """Extra distinct 829 for franchise"""
    return x
def extra_franchise_830(x):
    """Extra distinct 830 for franchise"""
    return x
def extra_franchise_831(x):
    """Extra distinct 831 for franchise"""
    return x
def extra_franchise_832(x):
    """Extra distinct 832 for franchise"""
    return x
def extra_franchise_833(x):
    """Extra distinct 833 for franchise"""
    return x
def extra_franchise_834(x):
    """Extra distinct 834 for franchise"""
    return x
def extra_franchise_835(x):
    """Extra distinct 835 for franchise"""
    return x
def extra_franchise_836(x):
    """Extra distinct 836 for franchise"""
    return x
def extra_franchise_837(x):
    """Extra distinct 837 for franchise"""
    return x
def extra_franchise_838(x):
    """Extra distinct 838 for franchise"""
    return x
def extra_franchise_839(x):
    """Extra distinct 839 for franchise"""
    return x
def extra_franchise_840(x):
    """Extra distinct 840 for franchise"""
    return x
def extra_franchise_841(x):
    """Extra distinct 841 for franchise"""
    return x
def extra_franchise_842(x):
    """Extra distinct 842 for franchise"""
    return x
def extra_franchise_843(x):
    """Extra distinct 843 for franchise"""
    return x
def extra_franchise_844(x):
    """Extra distinct 844 for franchise"""
    return x
def extra_franchise_845(x):
    """Extra distinct 845 for franchise"""
    return x
def extra_franchise_846(x):
    """Extra distinct 846 for franchise"""
    return x
def extra_franchise_847(x):
    """Extra distinct 847 for franchise"""
    return x
def extra_franchise_848(x):
    """Extra distinct 848 for franchise"""
    return x
def extra_franchise_849(x):
    """Extra distinct 849 for franchise"""
    return x
def extra_franchise_850(x):
    """Extra distinct 850 for franchise"""
    return x
def extra_franchise_851(x):
    """Extra distinct 851 for franchise"""
    return x
def extra_franchise_852(x):
    """Extra distinct 852 for franchise"""
    return x
def extra_franchise_853(x):
    """Extra distinct 853 for franchise"""
    return x
def extra_franchise_854(x):
    """Extra distinct 854 for franchise"""
    return x
def extra_franchise_855(x):
    """Extra distinct 855 for franchise"""
    return x
def extra_franchise_856(x):
    """Extra distinct 856 for franchise"""
    return x
def extra_franchise_857(x):
    """Extra distinct 857 for franchise"""
    return x
def extra_franchise_858(x):
    """Extra distinct 858 for franchise"""
    return x
def extra_franchise_859(x):
    """Extra distinct 859 for franchise"""
    return x
def extra_franchise_860(x):
    """Extra distinct 860 for franchise"""
    return x
def extra_franchise_861(x):
    """Extra distinct 861 for franchise"""
    return x
def extra_franchise_862(x):
    """Extra distinct 862 for franchise"""
    return x
def extra_franchise_863(x):
    """Extra distinct 863 for franchise"""
    return x
def extra_franchise_864(x):
    """Extra distinct 864 for franchise"""
    return x
def extra_franchise_865(x):
    """Extra distinct 865 for franchise"""
    return x
def extra_franchise_866(x):
    """Extra distinct 866 for franchise"""
    return x
def extra_franchise_867(x):
    """Extra distinct 867 for franchise"""
    return x
def extra_franchise_868(x):
    """Extra distinct 868 for franchise"""
    return x
def extra_franchise_869(x):
    """Extra distinct 869 for franchise"""
    return x
def extra_franchise_870(x):
    """Extra distinct 870 for franchise"""
    return x
def extra_franchise_871(x):
    """Extra distinct 871 for franchise"""
    return x
def extra_franchise_872(x):
    """Extra distinct 872 for franchise"""
    return x
def extra_franchise_873(x):
    """Extra distinct 873 for franchise"""
    return x
def extra_franchise_874(x):
    """Extra distinct 874 for franchise"""
    return x
def extra_franchise_875(x):
    """Extra distinct 875 for franchise"""
    return x
def extra_franchise_876(x):
    """Extra distinct 876 for franchise"""
    return x
def extra_franchise_877(x):
    """Extra distinct 877 for franchise"""
    return x
def extra_franchise_878(x):
    """Extra distinct 878 for franchise"""
    return x
def extra_franchise_879(x):
    """Extra distinct 879 for franchise"""
    return x
def extra_franchise_880(x):
    """Extra distinct 880 for franchise"""
    return x
def extra_franchise_881(x):
    """Extra distinct 881 for franchise"""
    return x
def extra_franchise_882(x):
    """Extra distinct 882 for franchise"""
    return x
def extra_franchise_883(x):
    """Extra distinct 883 for franchise"""
    return x
def extra_franchise_884(x):
    """Extra distinct 884 for franchise"""
    return x
def extra_franchise_885(x):
    """Extra distinct 885 for franchise"""
    return x
def extra_franchise_886(x):
    """Extra distinct 886 for franchise"""
    return x
def extra_franchise_887(x):
    """Extra distinct 887 for franchise"""
    return x
def extra_franchise_888(x):
    """Extra distinct 888 for franchise"""
    return x
def extra_franchise_889(x):
    """Extra distinct 889 for franchise"""
    return x
def extra_franchise_890(x):
    """Extra distinct 890 for franchise"""
    return x
def extra_franchise_891(x):
    """Extra distinct 891 for franchise"""
    return x
def extra_franchise_892(x):
    """Extra distinct 892 for franchise"""
    return x
def extra_franchise_893(x):
    """Extra distinct 893 for franchise"""
    return x
def extra_franchise_894(x):
    """Extra distinct 894 for franchise"""
    return x
def extra_franchise_895(x):
    """Extra distinct 895 for franchise"""
    return x
def extra_franchise_896(x):
    """Extra distinct 896 for franchise"""
    return x
def extra_franchise_897(x):
    """Extra distinct 897 for franchise"""
    return x
def extra_franchise_898(x):
    """Extra distinct 898 for franchise"""
    return x
def extra_franchise_899(x):
    """Extra distinct 899 for franchise"""
    return x
def extra_franchise_900(x):
    """Extra distinct 900 for franchise"""
    return x
def extra_franchise_901(x):
    """Extra distinct 901 for franchise"""
    return x
def extra_franchise_902(x):
    """Extra distinct 902 for franchise"""
    return x
def extra_franchise_903(x):
    """Extra distinct 903 for franchise"""
    return x
def extra_franchise_904(x):
    """Extra distinct 904 for franchise"""
    return x
def extra_franchise_905(x):
    """Extra distinct 905 for franchise"""
    return x
def extra_franchise_906(x):
    """Extra distinct 906 for franchise"""
    return x
def extra_franchise_907(x):
    """Extra distinct 907 for franchise"""
    return x
def extra_franchise_908(x):
    """Extra distinct 908 for franchise"""
    return x
def extra_franchise_909(x):
    """Extra distinct 909 for franchise"""
    return x
def extra_franchise_910(x):
    """Extra distinct 910 for franchise"""
    return x
def extra_franchise_911(x):
    """Extra distinct 911 for franchise"""
    return x
def extra_franchise_912(x):
    """Extra distinct 912 for franchise"""
    return x
def extra_franchise_913(x):
    """Extra distinct 913 for franchise"""
    return x
def extra_franchise_914(x):
    """Extra distinct 914 for franchise"""
    return x
def extra_franchise_915(x):
    """Extra distinct 915 for franchise"""
    return x
def extra_franchise_916(x):
    """Extra distinct 916 for franchise"""
    return x
def extra_franchise_917(x):
    """Extra distinct 917 for franchise"""
    return x
def extra_franchise_918(x):
    """Extra distinct 918 for franchise"""
    return x
def extra_franchise_919(x):
    """Extra distinct 919 for franchise"""
    return x
def extra_franchise_920(x):
    """Extra distinct 920 for franchise"""
    return x
def extra_franchise_921(x):
    """Extra distinct 921 for franchise"""
    return x
def extra_franchise_922(x):
    """Extra distinct 922 for franchise"""
    return x
def extra_franchise_923(x):
    """Extra distinct 923 for franchise"""
    return x
def extra_franchise_924(x):
    """Extra distinct 924 for franchise"""
    return x
def extra_franchise_925(x):
    """Extra distinct 925 for franchise"""
    return x
def extra_franchise_926(x):
    """Extra distinct 926 for franchise"""
    return x
def extra_franchise_927(x):
    """Extra distinct 927 for franchise"""
    return x
def extra_franchise_928(x):
    """Extra distinct 928 for franchise"""
    return x
def extra_franchise_929(x):
    """Extra distinct 929 for franchise"""
    return x
def extra_franchise_930(x):
    """Extra distinct 930 for franchise"""
    return x
def extra_franchise_931(x):
    """Extra distinct 931 for franchise"""
    return x
def extra_franchise_932(x):
    """Extra distinct 932 for franchise"""
    return x
def extra_franchise_933(x):
    """Extra distinct 933 for franchise"""
    return x
def extra_franchise_934(x):
    """Extra distinct 934 for franchise"""
    return x
def extra_franchise_935(x):
    """Extra distinct 935 for franchise"""
    return x
def extra_franchise_936(x):
    """Extra distinct 936 for franchise"""
    return x
def extra_franchise_937(x):
    """Extra distinct 937 for franchise"""
    return x
def extra_franchise_938(x):
    """Extra distinct 938 for franchise"""
    return x
def extra_franchise_939(x):
    """Extra distinct 939 for franchise"""
    return x
def extra_franchise_940(x):
    """Extra distinct 940 for franchise"""
    return x
def extra_franchise_941(x):
    """Extra distinct 941 for franchise"""
    return x
def extra_franchise_942(x):
    """Extra distinct 942 for franchise"""
    return x
def extra_franchise_943(x):
    """Extra distinct 943 for franchise"""
    return x
def extra_franchise_944(x):
    """Extra distinct 944 for franchise"""
    return x
def extra_franchise_945(x):
    """Extra distinct 945 for franchise"""
    return x
def extra_franchise_946(x):
    """Extra distinct 946 for franchise"""
    return x
def extra_franchise_947(x):
    """Extra distinct 947 for franchise"""
    return x
def extra_franchise_948(x):
    """Extra distinct 948 for franchise"""
    return x
def extra_franchise_949(x):
    """Extra distinct 949 for franchise"""
    return x
def extra_franchise_950(x):
    """Extra distinct 950 for franchise"""
    return x
def extra_franchise_951(x):
    """Extra distinct 951 for franchise"""
    return x
def extra_franchise_952(x):
    """Extra distinct 952 for franchise"""
    return x
def extra_franchise_953(x):
    """Extra distinct 953 for franchise"""
    return x
def extra_franchise_954(x):
    """Extra distinct 954 for franchise"""
    return x
def extra_franchise_955(x):
    """Extra distinct 955 for franchise"""
    return x
def extra_franchise_956(x):
    """Extra distinct 956 for franchise"""
    return x
def extra_franchise_957(x):
    """Extra distinct 957 for franchise"""
    return x
def extra_franchise_958(x):
    """Extra distinct 958 for franchise"""
    return x
def extra_franchise_959(x):
    """Extra distinct 959 for franchise"""
    return x
def extra_franchise_960(x):
    """Extra distinct 960 for franchise"""
    return x
def extra_franchise_961(x):
    """Extra distinct 961 for franchise"""
    return x
def extra_franchise_962(x):
    """Extra distinct 962 for franchise"""
    return x
def extra_franchise_963(x):
    """Extra distinct 963 for franchise"""
    return x
def extra_franchise_964(x):
    """Extra distinct 964 for franchise"""
    return x
def extra_franchise_965(x):
    """Extra distinct 965 for franchise"""
    return x
def extra_franchise_966(x):
    """Extra distinct 966 for franchise"""
    return x
def extra_franchise_967(x):
    """Extra distinct 967 for franchise"""
    return x
def extra_franchise_968(x):
    """Extra distinct 968 for franchise"""
    return x
def extra_franchise_969(x):
    """Extra distinct 969 for franchise"""
    return x
def extra_franchise_970(x):
    """Extra distinct 970 for franchise"""
    return x
def extra_franchise_971(x):
    """Extra distinct 971 for franchise"""
    return x
def extra_franchise_972(x):
    """Extra distinct 972 for franchise"""
    return x
def extra_franchise_973(x):
    """Extra distinct 973 for franchise"""
    return x
def extra_franchise_974(x):
    """Extra distinct 974 for franchise"""
    return x
def extra_franchise_975(x):
    """Extra distinct 975 for franchise"""
    return x
def extra_franchise_976(x):
    """Extra distinct 976 for franchise"""
    return x
def extra_franchise_977(x):
    """Extra distinct 977 for franchise"""
    return x
def extra_franchise_978(x):
    """Extra distinct 978 for franchise"""
    return x
def extra_franchise_979(x):
    """Extra distinct 979 for franchise"""
    return x
def extra_franchise_980(x):
    """Extra distinct 980 for franchise"""
    return x
def extra_franchise_981(x):
    """Extra distinct 981 for franchise"""
    return x
def extra_franchise_982(x):
    """Extra distinct 982 for franchise"""
    return x
def extra_franchise_983(x):
    """Extra distinct 983 for franchise"""
    return x
def extra_franchise_984(x):
    """Extra distinct 984 for franchise"""
    return x
def extra_franchise_985(x):
    """Extra distinct 985 for franchise"""
    return x
def extra_franchise_986(x):
    """Extra distinct 986 for franchise"""
    return x
def extra_franchise_987(x):
    """Extra distinct 987 for franchise"""
    return x
def extra_franchise_988(x):
    """Extra distinct 988 for franchise"""
    return x
def extra_franchise_989(x):
    """Extra distinct 989 for franchise"""
    return x
def extra_franchise_990(x):
    """Extra distinct 990 for franchise"""
    return x
def extra_franchise_991(x):
    """Extra distinct 991 for franchise"""
    return x
