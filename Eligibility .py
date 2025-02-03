import csv
import requests
import json
import time

# Madar Building Inventories
inv=[
        {"id" : 1, "price" : 60, "count" : 3396},
        {"id" : 2, "price" : 40, "count" : 13558},
        {"id" : 3, "price" : 180, "count" : 915},
        {"id" : 4, "price" : 80, "count" : 2475},
        {"id" : 5, "price" : 50, "count" : 840},
        {"id" : 6, "price" : 10, "count" : 47394},
        {"id" : 7, "price" : 50, "count" : 15021},
        {"id" : 8, "price" : 120, "count" : 1512},
        {"id" : 9, "price" : 30, "count" : 22508},
        {"id" : 10, "price" : 20, "count" : 8316},
        {"id" : 11, "price" : 190, "count" : 553},
        {"id" : 12, "price" : 60, "count" : 2055},
        {"id" : 13, "price" : 60, "count" : 1972},
        {"id" : 14, "price" : 30, "count" : 20392},
        {"id" : 15, "price" : 30, "count" : 35401},
        {"id" : 16, "price" : 50, "count" : 43010},
        {"id" : 17, "price" : 70, "count" : 8772},
        {"id" : 18, "price" : 40, "count" : 29026},
        {"id" : 19, "price" : 110, "count" : 3281},
        {"id" : 20, "price" : 70, "count" : 3497},
        {"id" : 21, "price" : 20, "count" : 23264},
        {"id" : 22, "price" : 50, "count" : 19394},
        {"id" : 23, "price" : 20, "count" : 10935},
        {"id" : 24, "price" : 40, "count" : 3672},
        {"id" : 25, "price" : 30, "count" : 995},
        {"id" : 26, "price" : 50, "count" : 3585},
        {"id" : 27, "price" : 50, "count" : 4982},
        {"id" : 28, "price" : 60, "count" : 1260},
        {"id" : 29, "price" : 40, "count" : 15732},
        {"id" : 30, "price" : 30, "count" : 2625},
        {"id" : 31, "price" : 40, "count" : 19727},
        {"id" : 32, "price" : 60, "count" : 9741},
        {"id" : 33, "price" : 70, "count" : 4219},
        {"id" : 34, "price" : 20, "count" : 59854},
        {"id" : 35, "price" : 30, "count" : 1151},
        {"id" : 36, "price" : 40, "count" : 1069},
        {"id" : 37, "price" : 40, "count" : 1439},
        {"id" : 38, "price" : 20, "count" : 2600},
        {"id" : 39, "price" : 20, "count" : 350},
        {"id" : 40, "price" : 30, "count" : 208},
        {"id" : 41, "price" : 20, "count" : 59},
        {"id" : 42, "price" : 20, "count" : 142},
        {"id" : 43, "price" : 20, "count" : 25},
        {"id" : 44, "price" : 20, "count" : 1645},
        {"id" : 45, "price" : 30, "count" : 102},
        {"id" : 46, "price" : 30, "count" : 24},
        {"id" : 47, "price" : 30, "count" : 195},
        {"id" : 48, "price" : 30, "count" : 96},
        {"id" : 49, "price" : 80, "count" : 22},
        {"id" : 50, "price" : 50, "count" : 468},
        {"id" : 51, "price" : 60, "count" : 1305},
        {"id" : 52, "price" : 40, "count" : 326},
        {"id" : 53, "price" : 110, "count" : 15},
        {"id" : 54, "price" : 90, "count" : 373},
        {"id" : 55, "price" : 40, "count" : 306},
        {"id" : 56, "price" : 110, "count" : 1769},
        {"id" : 57, "price" : 20, "count" : 245},
        {"id" : 58, "price" : 160, "count" : 772},
        {"id" : 59, "price" : 30, "count" : 44},
        {"id" : 60, "price" : 60, "count" : 6782},
        {"id" : 61, "price" : 150, "count" : 12},
        {"id" : 62, "price" : 30, "count" : 1658},
        {"id" : 63, "price" : 10, "count" : 27},
        {"id" : 64, "price" : 10, "count" : 50},
        {"id" : 65, "price" : 160, "count" : 13},
        {"id" : 66, "price" : 10, "count" : 213},
        {"id" : 67, "price" : 30, "count" : 100},
        {"id" : 68, "price" : 80, "count" : 19},
        {"id" : 69, "price" : 10, "count" : 500},
        {"id" : 70, "price" : 40, "count" : 101},
        {"id" : 71, "price" : 100, "count" : 122},
        {"id" : 72, "price" : 10, "count" : 700},
        {"id" : 73, "price" : 130, "count" : 126},
        {"id" : 74, "price" : 30, "count" : 41},
        {"id" : 75, "price" : 190, "count" : 36},
        {"id" : 76, "price" : 10, "count" : 26},
        {"id" : 77, "price" : 390, "count" : 40},
        {"id" : 78, "price" : 20, "count" : 123},
        {"id" : 79, "price" : 20, "count" : 31},
        {"id" : 80, "price" : 30, "count" : 1422},
        {"id" : 81, "price" : 180, "count" : 10},
        {"id" : 82, "price" : 60, "count" : 53},
        {"id" : 83, "price" : 80, "count" : 166},
        {"id" : 84, "price" : 140, "count" : 16},
        {"id" : 85, "price" : 80, "count" : 90},
        {"id" : 86, "price" : 110, "count" : 48},
        {"id" : 87, "price" : 160, "count" : 169},
        {"id" : 88, "price" : 210, "count" : 435},
        {"id" : 89, "price" : 40, "count" : 119},
        {"id" : 90, "price" : 210, "count" : 54},
        {"id" : 91, "price" : 60, "count" : 99},
        {"id" : 92, "price" : 70, "count" : 32},
        {"id" : 93, "price" : 60, "count" : 16},
        {"id" : 94, "price" : 80, "count" : 35},
        {"id" : 95, "price" : 80, "count" : 154},
        {"id" : 96, "price" : 100, "count" : 15},
        {"id" : 97, "price" : 200, "count" : 344},
        {"id" : 98, "price" : 100, "count" : 26},
        {"id" : 99, "price" : 180, "count" : 101},
        {"id" : 100, "price" : 260, "count" : 176},
        {"id" : 101, "price" : 980, "count" : 18},
        {"id" : 102, "price" : 50, "count" : 576},
        {"id" : 103, "price" : 130, "count" : 125},
        {"id" : 104, "price" : 60, "count" : 920},
        {"id" : 105, "price" : 190, "count" : 76},
        {"id" : 106, "price" : 110, "count" : 310},
        {"id" : 107, "price" : 60, "count" : 272},
        {"id" : 108, "price" : 20, "count" : 200},
        {"id" : 109, "price" : 40, "count" : 88},
        {"id" : 110, "price" : 70, "count" : 333},
        {"id" : 111, "price" : 50, "count" : 62},
        {"id" : 112, "price" : 80, "count" : 740},
        {"id" : 113, "price" : 20, "count" : 57},
        {"id" : 114, "price" : 80, "count" : 440},
        {"id" : 115, "price" : 70, "count" : 52},
        {"id" : 116, "price" : 30, "count" : 2870},
        {"id" : 117, "price" : 90, "count" : 1800},
        {"id" : 118, "price" : 100, "count" : 432},
        {"id" : 119, "price" : 30, "count" : 222},
        {"id" : 120, "price" : 100, "count" : 598},
        {"id" : 121, "price" : 130, "count" : 320},
        {"id" : 122, "price" : 110, "count" : 630},
        {"id" : 123, "price" : 30, "count" : 414},
        {"id" : 124, "price" : 80, "count" : 648},
        {"id" : 125, "price" : 60, "count" : 116},
        {"id" : 126, "price" : 30, "count" : 63},
        {"id" : 127, "price" : 80, "count" : 245},
        {"id" : 128, "price" : 90, "count" : 408},
        {"id" : 129, "price" : 40, "count" : 300},
        {"id" : 130, "price" : 60, "count" : 24},
        {"id" : 131, "price" : 80, "count" : 100},
        {"id" : 132, "price" : 50, "count" : 295},
        {"id" : 133, "price" : 70, "count" : 540},
        {"id" : 134, "price" : 80, "count" : 850},
        {"id" : 135, "price" : 100, "count" : 484},
        {"id" : 136, "price" : 140, "count" : 492},
        {"id" : 137, "price" : 30, "count" : 256},
        {"id" : 138, "price" : 40, "count" : 104},
        {"id" : 139, "price" : 40, "count" : 4012},
        {"id" : 140, "price" : 50, "count" : 28},
        {"id" : 141, "price" : 50, "count" : 2463},
        {"id" : 142, "price" : 120, "count" : 15},
        {"id" : 143, "price" : 60, "count" : 399},
        {"id" : 144, "price" : 130, "count" : 24},
        {"id" : 145, "price" : 90, "count" : 248},
        {"id" : 146, "price" : 50, "count" : 4514},
        {"id" : 147, "price" : 60, "count" : 62},
        {"id" : 148, "price" : 60, "count" : 1557},
        {"id" : 149, "price" : 80, "count" : 1657},
        {"id" : 150, "price" : 160, "count" : 70},
        {"id" : 151, "price" : 90, "count" : 167},
        {"id" : 152, "price" : 120, "count" : 22},
        {"id" : 153, "price" : 20, "count" : 303},
        {"id" : 154, "price" : 160, "count" : 56},
        {"id" : 155, "price" : 570, "count" : 48},
        {"id" : 156, "price" : 170, "count" : 13},
        {"id" : 157, "price" : 1970, "count" : 18},
        {"id" : 158, "price" : 3300, "count" : 32},
        {"id" : 159, "price" : 20, "count" : 109},
        {"id" : 160, "price" : 340, "count" : 30},
        {"id" : 161, "price" : 210, "count" : 43},
        {"id" : 162, "price" : 2230, "count" : 98},
        {"id" : 163, "price" : 30, "count" : 299},
        {"id" : 164, "price" : 3300, "count" : 55},
        {"id" : 165, "price" : 220, "count" : 46},
        {"id" : 166, "price" : 690, "count" : 100},
        {"id" : 167, "price" : 2430, "count" : 96},
        {"id" : 168, "price" : 1750, "count" : 84},
        {"id" : 169, "price" : 3300, "count" : 17},
        {"id" : 170, "price" : 20, "count" : 77},
        {"id" : 171, "price" : 2590, "count" : 102},
        {"id" : 172, "price" : 3100, "count" : 83},
        {"id" : 173, "price" : 240, "count" : 11},
        {"id" : 174, "price" : 280, "count" : 36},
        {"id" : 175, "price" : 30, "count" : 210},
        {"id" : 176, "price" : 1250, "count" : 35},
        {"id" : 177, "price" : 320, "count" : 12},
        {"id" : 178, "price" : 350, "count" : 15},
        {"id" : 179, "price" : 3150, "count" : 68},
        {"id" : 180, "price" : 2840, "count" : 36},
        {"id" : 181, "price" : 1980, "count" : 70},
        {"id" : 182, "price" : 40, "count" : 10},
        {"id" : 183, "price" : 2850, "count" : 26},
        {"id" : 184, "price" : 3100, "count" : 39},
        {"id" : 185, "price" : 430, "count" : 95},
        {"id" : 186, "price" : 740, "count" : 115},
        {"id" : 187, "price" : 40, "count" : 276},
        {"id" : 188, "price" : 3780, "count" : 32},
        {"id" : 189, "price" : 3100, "count" : 65},
        {"id" : 190, "price" : 3300, "count" : 64},
        {"id" : 191, "price" : 880, "count" : 30},
        {"id" : 192, "price" : 440, "count" : 34},
        {"id" : 193, "price" : 30, "count" : 109},
        {"id" : 194, "price" : 3100, "count" : 125},
        {"id" : 195, "price" : 190, "count" : 32},
        {"id" : 196, "price" : 1040, "count" : 70},
        {"id" : 197, "price" : 3300, "count" : 63},
        {"id" : 198, "price" : 420, "count" : 13},
        {"id" : 199, "price" : 570, "count" : 29},
        {"id" : 200, "price" : 4640, "count" : 144},
        {"id" : 201, "price" : 1220, "count" : 320},
        {"id" : 202, "price" : 3300, "count" : 20},
        {"id" : 203, "price" : 40, "count" : 24},
        {"id" : 204, "price" : 830, "count" : 40},
        {"id" : 205, "price" : 580, "count" : 20},
        {"id" : 206, "price" : 1430, "count" : 33},
        {"id" : 207, "price" : 3300, "count" : 158},
        {"id" : 208, "price" : 5190, "count" : 33},
        {"id" : 209, "price" : 1010, "count" : 21},
        {"id" : 210, "price" : 3100, "count" : 46},
        {"id" : 211, "price" : 40, "count" : 253},
        {"id" : 212, "price" : 710, "count" : 26},
        {"id" : 213, "price" : 5310, "count" : 20},
        {"id" : 214, "price" : 1680, "count" : 324},
        {"id" : 215, "price" : 3100, "count" : 47},
        {"id" : 216, "price" : 2520, "count" : 14},
        {"id" : 217, "price" : 30, "count" : 448},
        {"id" : 218, "price" : 1980, "count" : 24},
        {"id" : 219, "price" : 730, "count" : 12},
        {"id" : 220, "price" : 3100, "count" : 23},
        {"id" : 221, "price" : 5630, "count" : 25},
        {"id" : 222, "price" : 2270, "count" : 163},
        {"id" : 223, "price" : 3500, "count" : 87},
        {"id" : 224, "price" : 40, "count" : 264},
        {"id" : 225, "price" : 870, "count" : 10},
        {"id" : 226, "price" : 3650, "count" : 37},
        {"id" : 227, "price" : 2630, "count" : 220},
        {"id" : 228, "price" : 6140, "count" : 145},
        {"id" : 229, "price" : 4180, "count" : 103},
        {"id" : 230, "price" : 1160, "count" : 14},
        {"id" : 231, "price" : 3500, "count" : 27},
        {"id" : 232, "price" : 50, "count" : 50},
        {"id" : 233, "price" : 7410, "count" : 89},
        {"id" : 234, "price" : 3500, "count" : 11},
        {"id" : 235, "price" : 1590, "count" : 19},
        {"id" : 236, "price" : 3650, "count" : 71},
        {"id" : 237, "price" : 8780, "count" : 63},
        {"id" : 238, "price" : 3080, "count" : 126},
        {"id" : 239, "price" : 1990, "count" : 12},
        {"id" : 240, "price" : 3500, "count" : 33},
        {"id" : 241, "price" : 4910, "count" : 19},
        {"id" : 242, "price" : 1740, "count" : 23},
        {"id" : 243, "price" : 3500, "count" : 44},
        {"id" : 244, "price" : 3180, "count" : 11},
        {"id" : 245, "price" : 780, "count" : 49},
        {"id" : 246, "price" : 3650, "count" : 37},
        {"id" : 247, "price" : 10560, "count" : 24},
        {"id" : 248, "price" : 890, "count" : 15},
        {"id" : 249, "price" : 2090, "count" : 12},
        {"id" : 250, "price" : 3500, "count" : 28},
        {"id" : 251, "price" : 1280, "count" : 45},
        {"id" : 252, "price" : 13000, "count" : 11},
        {"id" : 253, "price" : 3500, "count" : 36},
        {"id" : 254, "price" : 2510, "count" : 52},
        {"id" : 255, "price" : 1750, "count" : 76},
        {"id" : 256, "price" : 3500, "count" : 29},
        {"id" : 257, "price" : 60, "count" : 14},
        {"id" : 258, "price" : 16250, "count" : 51},
        {"id" : 259, "price" : 2920, "count" : 30},
        {"id" : 260, "price" : 4400, "count" : 40},
        {"id" : 261, "price" : 2010, "count" : 20},
        {"id" : 262, "price" : 19500, "count" : 16},
        {"id" : 263, "price" : 80, "count" : 136},
        {"id" : 264, "price" : 4400, "count" : 49},
        {"id" : 265, "price" : 3400, "count" : 32},
        {"id" : 266, "price" : 40, "count" : 278},
        {"id" : 267, "price" : 4400, "count" : 72},
        {"id" : 268, "price" : 50, "count" : 24},
        {"id" : 269, "price" : 4780, "count" : 95},
        {"id" : 270, "price" : 4400, "count" : 57},
        {"id" : 271, "price" : 50, "count" : 125},
        {"id" : 272, "price" : 70, "count" : 15},
        {"id" : 273, "price" : 4400, "count" : 61},
        {"id" : 274, "price" : 6330, "count" : 29},
        {"id" : 275, "price" : 50, "count" : 24},
        {"id" : 276, "price" : 4400, "count" : 357},
        {"id" : 277, "price" : 60, "count" : 16},
        {"id" : 278, "price" : 6980, "count" : 28},
        {"id" : 279, "price" : 4400, "count" : 311},
        {"id" : 280, "price" : 50, "count" : 15},
        {"id" : 281, "price" : 2330, "count" : 110},
        {"id" : 282, "price" : 70, "count" : 25},
        {"id" : 283, "price" : 4400, "count" : 242},
        {"id" : 284, "price" : 7630, "count" : 33},
        {"id" : 285, "price" : 60, "count" : 15},
        {"id" : 286, "price" : 2710, "count" : 106},
        {"id" : 287, "price" : 4400, "count" : 108},
        {"id" : 288, "price" : 100, "count" : 86},
        {"id" : 289, "price" : 3170, "count" : 64},
        {"id" : 290, "price" : 8910, "count" : 48},
        {"id" : 291, "price" : 70, "count" : 13},
        {"id" : 292, "price" : 4400, "count" : 196},
        {"id" : 293, "price" : 3710, "count" : 17},
        {"id" : 294, "price" : 4400, "count" : 65},
        {"id" : 295, "price" : 50, "count" : 45},
        {"id" : 296, "price" : 90, "count" : 13},
        {"id" : 297, "price" : 100, "count" : 12},
        {"id" : 298, "price" : 4980, "count" : 21},
        {"id" : 299, "price" : 4400, "count" : 15},
        {"id" : 300, "price" : 160, "count" : 17},
        {"id" : 301, "price" : 130, "count" : 15},
        {"id" : 302, "price" : 980, "count" : 14},
        {"id" : 303, "price" : 4400, "count" : 34},
        {"id" : 304, "price" : 60, "count" : 47},
        {"id" : 305, "price" : 1210, "count" : 135},
        {"id" : 306, "price" : 4400, "count" : 45},
        {"id" : 307, "price" : 150, "count" : 11},
        {"id" : 308, "price" : 40, "count" : 19},
        {"id" : 309, "price" : 1410, "count" : 28},
        {"id" : 310, "price" : 4800, "count" : 63},
        {"id" : 311, "price" : 80, "count" : 14},
        {"id" : 312, "price" : 140, "count" : 24},
        {"id" : 313, "price" : 50, "count" : 15},
        {"id" : 314, "price" : 580, "count" : 138},
        {"id" : 315, "price" : 1680, "count" : 245},
        {"id" : 316, "price" : 80, "count" : 152},
        {"id" : 317, "price" : 210, "count" : 161},
        {"id" : 318, "price" : 2430, "count" : 14},
        {"id" : 319, "price" : 60, "count" : 16},
        {"id" : 320, "price" : 690, "count" : 14},
        {"id" : 321, "price" : 150, "count" : 17},
        {"id" : 322, "price" : 2710, "count" : 51},
        {"id" : 323, "price" : 410, "count" : 15},
        {"id" : 324, "price" : 70, "count" : 42},
        {"id" : 325, "price" : 3030, "count" : 22},
        {"id" : 326, "price" : 470, "count" : 30},
        {"id" : 327, "price" : 80, "count" : 22},
        {"id" : 328, "price" : 520, "count" : 16},
        {"id" : 329, "price" : 3500, "count" : 199},
        {"id" : 330, "price" : 710, "count" : 34},
        {"id" : 331, "price" : 3870, "count" : 19},
        {"id" : 332, "price" : 850, "count" : 16},
        {"id" : 333, "price" : 90, "count" : 32},
        {"id" : 334, "price" : 130, "count" : 11},
        {"id" : 335, "price" : 10, "count" : 255},
        {"id" : 336, "price" : 4160, "count" : 22},
        {"id" : 337, "price" : 1360, "count" : 120},
        {"id" : 338, "price" : 170, "count" : 49},
        {"id" : 339, "price" : 4440, "count" : 16},
        {"id" : 340, "price" : 100, "count" : 28},
        {"id" : 341, "price" : 20, "count" : 81},
        {"id" : 342, "price" : 20, "count" : 11},
        {"id" : 343, "price" : 5550, "count" : 65},
        {"id" : 344, "price" : 280, "count" : 24},
        {"id" : 345, "price" : 340, "count" : 108},
        {"id" : 346, "price" : 30, "count" : 10},
        {"id" : 347, "price" : 6330, "count" : 13},
        {"id" : 348, "price" : 440, "count" : 12},
        {"id" : 349, "price" : 50, "count" : 33},
        {"id" : 350, "price" : 30, "count" : 500},
        {"id" : 351, "price" : 7480, "count" : 44},
        {"id" : 352, "price" : 210, "count" : 15},
        {"id" : 353, "price" : 1010, "count" : 15},
        {"id" : 354, "price" : 40, "count" : 32},
        {"id" : 355, "price" : 30, "count" : 52},
        {"id" : 356, "price" : 60, "count" : 13},
        {"id" : 357, "price" : 410, "count" : 54},
        {"id" : 358, "price" : 1250, "count" : 31},
        {"id" : 359, "price" : 50, "count" : 24},
        {"id" : 360, "price" : 1730, "count" : 198},
        {"id" : 361, "price" : 270, "count" : 136},
        {"id" : 362, "price" : 50, "count" : 27},
        {"id" : 363, "price" : 2470, "count" : 26},
        {"id" : 364, "price" : 40, "count" : 303},
        {"id" : 365, "price" : 530, "count" : 88},
        {"id" : 366, "price" : 3610, "count" : 50},
        {"id" : 367, "price" : 70, "count" : 17},
        {"id" : 368, "price" : 50, "count" : 126},
        {"id" : 369, "price" : 3990, "count" : 10},
        {"id" : 370, "price" : 700, "count" : 47},
        {"id" : 371, "price" : 80, "count" : 15},
        {"id" : 372, "price" : 4290, "count" : 25},
        {"id" : 373, "price" : 50, "count" : 864},
        {"id" : 374, "price" : 120, "count" : 15},
        {"id" : 375, "price" : 5110, "count" : 15},
        {"id" : 376, "price" : 820, "count" : 15},
        {"id" : 377, "price" : 3350, "count" : 27},
        {"id" : 378, "price" : 1340, "count" : 68},
        {"id" : 379, "price" : 60, "count" : 1179},
        {"id" : 380, "price" : 980, "count" : 17},
        {"id" : 381, "price" : 3250, "count" : 16},
        {"id" : 382, "price" : 500, "count" : 33},
        {"id" : 383, "price" : 60, "count" : 580},
        {"id" : 384, "price" : 3250, "count" : 49},
        {"id" : 385, "price" : 990, "count" : 213},
        {"id" : 386, "price" : 3250, "count" : 48},
        {"id" : 387, "price" : 1350, "count" : 13},
        {"id" : 388, "price" : 1680, "count" : 25},
        {"id" : 389, "price" : 70, "count" : 594},
        {"id" : 390, "price" : 1920, "count" : 121},
        {"id" : 391, "price" : 80, "count" : 564},
        {"id" : 392, "price" : 80, "count" : 13},
        {"id" : 393, "price" : 2110, "count" : 33},
        {"id" : 394, "price" : 30, "count" : 13},
        {"id" : 395, "price" : 550, "count" : 11},
        {"id" : 396, "price" : 1000, "count" : 409},
        {"id" : 397, "price" : 80, "count" : 121},
        {"id" : 398, "price" : 880, "count" : 16},
        {"id" : 399, "price" : 100, "count" : 137},
        {"id" : 400, "price" : 1150, "count" : 94},
        {"id" : 401, "price" : 130, "count" : 15},
        {"id" : 402, "price" : 1460, "count" : 68},
        {"id" : 403, "price" : 150, "count" : 48},
        {"id" : 404, "price" : 1640, "count" : 170},
        {"id" : 405, "price" : 1570, "count" : 24},
        {"id" : 406, "price" : 230, "count" : 21},
        {"id" : 407, "price" : 240, "count" : 21},
        {"id" : 408, "price" : 250, "count" : 44},
        {"id" : 409, "price" : 340, "count" : 60},
        {"id" : 410, "price" : 400, "count" : 17},
        {"id" : 411, "price" : 420, "count" : 21},
        {"id" : 412, "price" : 500, "count" : 37},
        {"id" : 413, "price" : 680, "count" : 29},
        {"id" : 414, "price" : 60, "count" : 120},
        {"id" : 415, "price" : 490, "count" : 24},
        {"id" : 416, "price" : 80, "count" : 11},
        {"id" : 417, "price" : 3210, "count" : 18},
        {"id" : 418, "price" : 420, "count" : 10},
        {"id" : 419, "price" : 4740, "count" : 21},
        {"id" : 420, "price" : 110, "count" : 18},
        {"id" : 421, "price" : 1710, "count" : 12},
        {"id" : 422, "price" : 550, "count" : 41},
        {"id" : 423, "price" : 5050, "count" : 13},
        {"id" : 424, "price" : 640, "count" : 15},
        {"id" : 425, "price" : 190, "count" : 36},
        {"id" : 426, "price" : 10100, "count" : 30},
        {"id" : 427, "price" : 6320, "count" : 30},
        {"id" : 428, "price" : 18940, "count" : 22},
        {"id" : 429, "price" : 230, "count" : 22},
        {"id" : 430, "price" : 880, "count" : 17},
        {"id" : 431, "price" : 9470, "count" : 25},
        {"id" : 432, "price" : 1610, "count" : 13},
        {"id" : 433, "price" : 250, "count" : 13},
        {"id" : 434, "price" : 1930, "count" : 26},
        {"id" : 435, "price" : 2570, "count" : 13},
        {"id" : 436, "price" : 290, "count" : 84},
        {"id" : 437, "price" : 380, "count" : 17},
        {"id" : 438, "price" : 50, "count" : 18},
        {"id" : 439, "price" : 2030, "count" : 12},
        {"id" : 440, "price" : 70, "count" : 85},
        {"id" : 441, "price" : 150, "count" : 20},
        {"id" : 442, "price" : 210, "count" : 24},
        {"id" : 443, "price" : 130, "count" : 16},
        {"id" : 444, "price" : 270, "count" : 10},
        {"id" : 445, "price" : 100, "count" : 16},
        {"id" : 446, "price" : 130, "count" : 23},
        {"id" : 447, "price" : 190, "count" : 12},
        {"id" : 448, "price" : 390, "count" : 79},
        {"id" : 449, "price" : 470, "count" : 31},
        
    ]

def find_item_by_id(item_id):
    for item in inv:
        if item["id"] == item_id:
            return item
    return None 

def isUsedCount(invetory):
  isUsedCount= False
  for item in invetory:
    used= item['used_count']
    actualCount=find_item_by_id(item['inventory_id'])["count"]
    if( used<=actualCount):
      isUsedCount= True
    else:
      isUsedCount= False
      return isUsedCount
  return isUsedCount 
  
def isInvPriceMatch(invetory):
  isInvPriceMatch= False
  for item in invetory:
    usedPrice= item['price']
    actualPrice=find_item_by_id(item['inventory_id'])["price"]
    if( usedPrice == actualPrice):
      isInvPriceMatch= True
    else:
      isInvPriceMatch= False
      return isInvPriceMatch
    
  return isInvPriceMatch
      
def isPriceMatch(invetory, totalPrice):
  priceSum=0
  for item in invetory:
    used= item['used_count']
    actualPrice=find_item_by_id(item['inventory_id'])["price"]
    priceSum=priceSum+(used*actualPrice)
  return priceSum == totalPrice 

def isTotalPriceMatch(invetory, totalPrice):
  priceSum=0
  for item in invetory:
    invPrice= item['total_price']
    priceSum=priceSum+invPrice   
  return priceSum == totalPrice 

def isTotalPriceVsLoan(total,loan):
  return float(total) == float(loan)
  

def send_post_request(loan, url):
  headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  }


  data = {
    "loan": loan,
    "inventories": inv
}
  response = requests.post(url, headers=headers, data=json.dumps(data))

  if response.status_code == 200:
    print("Request successful")
    print(response.json())
    return(response.json(), response.status_code)
  else:
    print("Request failed with status code:", response.status_code)
    print(response.text)
    return(response.json() ,response.status_code)
 
   
StartTime= time.time()

url = "https://dev-api.uselynk.com/api/v1/test/loan-coverage"
timestr = time.strftime("%Y%m%d-%H%M%S")

input_file = 'input.csv' 
output_file = f'output_{timestr}.csv'

with open(output_file, 'w', newline='') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(['Loan', 'covered/uncovered','elapsed_time','reStatus','msg','OutputInvCount_VS_InputInvCount','OutputInvPrice_VS_InputInvPrice','OutputOrdTotalPrice_VS_InputSumInvPriceX','OutputOrdTotalPrice_VS_InputSumInvTotalPrice','OutputOrdTotalPrice_VS_InputLoan','OutputTotalUnits'])
    with open(input_file, newline='') as in_csv:
        reader = csv.reader(in_csv)       
        next(reader)
        
        for row in reader:                
            price = row[0]
            response,resStatus = send_post_request(float(price), url)
            if(resStatus == 200 and  response['status'] == "covered"):
                status = response['status']
                elapsed_time = response['elapsed_time']                
                writer.writerow([price, status,elapsed_time,resStatus,"N/A",isUsedCount(response["inventories"]) ,isInvPriceMatch(response["inventories"]),isPriceMatch(response["inventories"],response['total_price']), isTotalPriceMatch(response["inventories"],response['total_price']),isTotalPriceVsLoan(price,response['total_price']),response["used_units"]])
                
            else:
              status = response['status']
              elapsed_time = response['elapsed_time']
              msg="N/A"
              if(resStatus != 200):
                msg=response["extra"]["msg"]
              writer.writerow([price, status, elapsed_time,resStatus,msg,"N/A","N/A","N/A","N/A","N/A","N/A"])
            # time.sleep(1)  
            
            
EndtTime= time.time()
print(f'Total Time: '+ str(EndtTime - StartTime))
