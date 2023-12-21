import os
import gdown

gdrive_ids = [
    # {"name": "posts_image.z01", "id":"1onMB9QKmEs1Rud1Lb5QU_NjItqSOs-3w"},
    # {"name": "posts_image.z02", "id":"1VkwQBdYu1Iqh_QFxd2VcPG2U0ZhEHtWJ"},
    {"name": "posts_image.z03", "id":"1Jf-BetMjUiRdbTI4UKVNKtHoNbksLoOu"},
    # {"name": "posts_image.z04", "id":"1PdQhxmvAxIoJEeKiqgR2es5oSf3ASx0_"},
    # {"name": "posts_image.z05", "id":"1D3BtDoqx1ODxRnCeLvxtXXpU3KovSWPp"},
    # {"name": "posts_image.z06", "id":"1BMIynWZ_btDs9GiQ2j0aVVlrx03H-cKb"},
    # {"name": "posts_image.z07", "id":"16vcB3KfEARIXFo81Gzf12UjKIj7_z-Yy"},
    # {"name": "posts_image.z08", "id":"1-v1IuXMUwV1wehAETqyAYEN31xWB_q2B"},
    # {"name": "posts_image.z09", "id":"1jDPaGB5uNM6jhjEz0SxWpEaDSYOIkktw"},
    # {"name": "posts_image.z10", "id":"1lv-01-BbcI-pTe6VJjmJ1w9PYsMElxOt"},
    # {"name": "posts_image.z11", "id":"1lU6CFXIgxh5EjMkwCnVfo1SYHKVV-Mhd"},
    {"name": "posts_image.z12", "id":"1vTs5WrZiFW_5NLL8GzlHiFA7_hrRuQmK"},
    # {"name": "posts_image.z13", "id":"1vsv92Ma6aPa7qmFpze4eXB0eIVpQFEtM"},
    {"name": "posts_image.z14", "id":"12aKYHLnRiofU2j0epYjXA8VpKaYzXsWL"},
    {"name": "posts_image.z15", "id":"18mJcezHgQjg8WXWEZRNhrw3LUGICMBAl"},
    {"name": "posts_image.z16", "id":"1GwWh_v6JcsSQy7cKbY_8pUZZKzeruDho"},
    {"name": "posts_image.z17", "id":"1K0Kg3PF81JaKcsjdO5NCXr2eC6bnCx7a"},
    {"name": "posts_image.z18", "id":"1UkiJHjtwDTNiZAapTvev287Qtk2tJ4dv"},
    {"name": "posts_image.z19", "id":"11nzaBNho1ZyT-FCa790AFGLSWcYrot1s"},
    {"name": "posts_image.z20", "id":"1-QaR-ax1VmA_4so5hYfkpFBU1pkj5V-O"},
    {"name": "posts_image.z21", "id":"1MhGLFOHlM7Rd617GCzYQNRtY6xa-_anW"},
    {"name": "posts_image.z22", "id":"1qVQS5QqUHVI7hsOTV6NHA_K8Rt-RKbWR"},
    {"name": "posts_image.z23", "id":"1Q6mCGW02x0JG0F9WhIVJAWDO9uaKsJdI"},
    {"name": "posts_image.z24", "id":"1EoGHAcmdcR1ANmDo2TGP6UjuZpjbw_R0"},
    {"name": "posts_image.z25", "id":"1G38SfiuhLGrFJsINpccMAoa75ZbrZ91f"},
    {"name": "posts_image.z26", "id":"19VaPJhgRv8XCODweYjMmfGY7n8UVvxG5"},
    {"name": "posts_image.z27", "id":"1uFBqRoEPhz650fYea4nMiZAkRTSX-PuU"},
    {"name": "posts_image.z28", "id":"1iBOfZ1ar2xlL8lvs2f9vsHgSfOIK8RMg"},
    {"name": "posts_image.z29", "id":"1yuHbWWCfK8m2XnAvL7zuUDMvnkQzDX2m"},
    {"name": "posts_image.z30", "id":"1vUfv0XQDjsZ0BarCF48Mty3byRz5YHHP"},
    {"name": "posts_image.z31", "id":"1E0ZDUyIDwSmJy4X9ydOdKiFFJbDUBEw3"},

    {"name": "posts_image.z32", "id":"1IwG3dEPIsTl5pO2KzTEdmUsSmCTqz0u1"},
    {"name": "posts_image.z33", "id":"17nv8VqCdaKOZW3EsY9qCucTZdA3rk0Be"},
    {"name": "posts_image.z34", "id":"1hlD9IpBVjRvSyBOUE8Msh65jg-xPlZaz"},
    {"name": "posts_image.z35", "id":"17TXlVIkGeq-VUzMKRFWtcQeQA9NZBwaL"},
    {"name": "posts_image.z36", "id":"10bIoYOjWEe-Z94-p88w9i17Zsch_AZ77"},
    {"name": "posts_image.z37", "id":"1bSV0_aLiNdHNeq0AJj_XZFvyMhAiiu1y"},
    {"name": "posts_image.z38", "id":"1DRnU0OwrauwaeLrhMIua8FzG8usTAQZA"},
    {"name": "posts_image.z39", "id":"1VhuPlGM9A8ssrUJ7VoM4yh0oo2BjZjLD"},
    # {"name": "posts_image.z40", "id":"1Iyv5i0BHd1yS8tO3x8X_sdeINY07iMa4"},
    {"name": "posts_image.z41", "id":"1DOBYMHpnNio8yoSwkwMHeYb0Pd7wt4CT"},
    {"name": "posts_image.z42", "id":"1odvE1YuB9ZhMsiEFnoFA1y7zkfixX4Yx"},
    {"name": "posts_image.z43", "id":"12bja4PHUOUUEXJMz9FvQnrWBEfzrNXU_"},
    {"name": "posts_image.z44", "id":"1NkgjIVLEFDUkYKQlsZ1eqGht9oI_ZfHT"},
    {"name": "posts_image.z45", "id":"1Lk1XwpmmEA4eeCVzumKJU2hcMYwEvOFQ"},
    {"name": "posts_image.z46", "id":"1Nv-kKgQ7UzbMMqyojZOLnP6zHigZ29yq"},
    {"name": "posts_image.z47", "id":"1n81Xzx5wbpPuMSaOwJYIMtgiDWNUORof"},
    {"name": "posts_image.z48", "id":"1o_bZox_2S5OK_JY-WlN9Pyi0BjW_xQhc"},
    {"name": "posts_image.z49", "id":"1JZRUPYdwNWOpGN4TnocBe94rx-nnhqXU"},
    
    {"name": "posts_image.z50", "id":"1pkYuX2utYq-WVfVefYZm7WjWyL2W_QAm"},
    {"name": "posts_image.z51", "id":"136TgH5FT4JHnkbuhdggsODr6D9I0T99n"},
    {"name": "posts_image.z52", "id":"10cL5_ZZ_mOHIvZXf6Zm-5mveV55coNS0"},
    {"name": "posts_image.z53", "id":"1kLT8O9ksRaPoybb19J4ooQTIKImxVLOU"},
    {"name": "posts_image.z54", "id":"1DQR3mmL1yIebXzLkJuLzgP21ZCSjpiCq"},
    {"name": "posts_image.z55", "id":"1UJeJ5aG1igDc09njx03RUFQO8gURFcU5"},
    {"name": "posts_image.z56", "id":"1TKjqbvSVPjg-jn4HO4Qxac3LA2RfoGcG"},
    {"name": "posts_image.z57", "id":"1CEX6AVMXE94vFt-lw5y7wPWgd72p7DY2"},
    {"name": "posts_image.z58", "id":"1XkMGlP6rALvbY1iLxhRD2WsQq69odJF5"},
    {"name": "posts_image.z59", "id":"1aaCO_hGVKjV6EpSfJXjcktlcMzjOmiuf"},
    {"name": "posts_image.z60", "id":"1mHBltx3FhCuF_fXHI98unlpbgLBMOiNa"},
    {"name": "posts_image.z61", "id":"1nSQT_-rl-nNXRbTiCQ-9CsHYP_6VrkP-"},
    {"name": "posts_image.z62", "id":"1zRG2ex-xX6l8z4c0u01_BONQzRUcCnTG"},
    {"name": "posts_image.z63", "id":"1FLS3AQ_5pxHi7mY84xgtIt0Ev8zc9Oj8"},
]

for link in gdrive_ids:
    if os.path.exists(link['name']):
        print(f"{link['name']} exists")
    else:
        print(f"Downloading {link['name']}")
        gdown.download(id=link['id'])
