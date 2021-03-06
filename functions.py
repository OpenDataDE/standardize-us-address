
import usaddress


state_replacement_dict = {u'Mississippi': u'MS', u'Oklahoma': u'OK', u'Delaware': u'DE', u'Minnesota': u'MN', \
u'Illinois': u'IL', u'Arkansas': u'AR', u'New Mexico': u'NM', u'Indiana': u'IN', u'Maryland': u'MD', u'Louisiana': u'LA', \
u'Idaho': u'ID', u'Wyoming': u'WY', u'Tennessee': u'TN', u'Arizona': u'AZ', u'Iowa': u'IA', u'Michigan': u'MI', u'Kansas': u'KS', \
u'Utah': u'UT', u'Virginia': u'VA', u'Oregon': u'OR', u'Connecticut': u'CT', u'Montana': u'MT', u'California': u'CA', \
u'Massachusetts': u'MA', u'West Virginia': u'WV', u'South Carolina': u'SC', u'New Hampshire': u'NH', u'Wisconsin': u'WI', \
u'Vermont': u'VT', u'Georgia': u'GA', u'North Dakota': u'ND', u'Pennsylvania': u'PA', u'Florida': u'FL', u'Alaska': u'AK', \
u'Kentucky': u'KY', u'Hawaii': u'HI', u'Nebraska': u'NE', u'Missouri': u'MO', u'Ohio': u'OH', u'Alabama': u'AL', \
u'Rhode Island': u'RI', u'South Dakota': u'SD', u'Colorado': u'CO', u'New Jersey': u'NJ', u'Washington': u'WA', \
u'North Carolina': u'NC', u'New York': u'NY', u'District of Columbia': u'DC', u'Texas': u'TX', u'Nevada': u'NV', u'Maine': u'ME'}
state_replacement_dict['DC, DC'] = 'DC'
state_replacement_dict['DC, MD'] = 'DC'
state_replacement_dict['DE, DE'] = 'DE'
state_replacement_dict['DE DE'] = 'DE'

#state_replacement_dict[''] = ''



# Upper case the string before testing
# Generated from the USPS table at http://pe.usps.gov/text/pub28/28apc_002.htm
street_type_replacement_dict = {u'WLS': u'WLS', u'CPE': u'CPE', u'ORCHRD': u'ORCH', u'CRESCENT': u'CRES', u'FALL': u'FALL', \
u'BEACH': u'BCH', u'MSSN': u'MSN', u'RAMP': u'RAMP', u'KYS': u'KYS', u'SPG': u'SPG', u'JCTN': u'JCT', u'TUNEL': u'TUNL', \
u'PARKWAYS': u'PKWY', u'COVE': u'CV', u'BYP': u'BYP', u'SPRINGS': u'SPGS', u'ISLANDS': u'ISS', u'RIVER': u'RIV', u'SPUR': u'SPUR',\
u'JCTS': u'JCTS', u'VIADCT': u'VIA', u'PINES': u'PNES', u'EXPRESS': u'EXPY', u'MNRS': u'MNRS', u'TUNLS': u'TUNL', \
u'GROVES': u'GRVS', u'SUMITT': u'SMT', u'OVL': u'OVAL', u'VIEW': u'VW', u'CRSNT': u'CRES', u'PKWYS': u'PKWY', u'TRK': u'TRAK', \
u'THROUGHWAY': u'TRWY', u'SQUARE': u'SQ', u'CSWY': u'CSWY', u'CMP': u'CP', u'CENTR': u'CTR', u'VLG': u'VLG', u'VLY': u'VLY', \
u'FRD': u'FRD', u'COMMON': u'CMN', u'GRV': u'GRV', u'FLAT': u'FLT', u'LOAF': u'LF', u'JCTNS': u'JCTS', u'UNION': u'UN', \
u'BAYOO': u'BYU', u'DRIVES': u'DRS', u'BAYOU': u'BYU', u'GRN': u'GRN', u'FERRY': u'FRY', u'TRCE': u'TRCE', u'BLF': u'BLF', \
u'SPRNG': u'SPG', u'BYPAS': u'BYP', u'RADL': u'RADL', u'HLS': u'HLS', u'VWS': u'VWS', u'MT': u'MT', u'GRDN': u'GDN', u'FT': u'FT', \
u'GLN': u'GLN', u'CTS': u'CTS', u'SMT': u'SMT', u'KNOL': u'KNL', u'STATION': u'STA', u'BEND': u'BND', u'CORNER': u'COR', \
u'POINT': u'PT', u'SHL': u'SHL', u'MDW': u'MDWS', u'BURGS': u'BGS', u'ESTATE': u'EST', u'CRSENT': u'CRES', u'PLAIN': u'PLN', \
u'MOUNT': u'MT', u'MNTAIN': u'MTN', u'MEDOWS': u'MDWS', u'SPRNGS': u'SPGS', u'TURNPIKE': u'TPKE', u'CREEK': u'CRK', u'SQ': u'SQ', \
u'ST': u'ST', u'ALY': u'ALY', u'ROADS': u'RDS', u'RADIEL': u'RADL', u'OVERPASS': u'OPAS', u'TRLR': u'TRLR', u'TRLS': u'TRL', \
u'RIDGE': u'RDG', u'FORESTS': u'FRST', u'GREEN': u'GRN', u'LF': u'LF', u'GARDN': u'GDN', u'VDCT': u'VIA', u'LN': u'LN', \
u'PARKWY': u'PKWY', u'BLUFF': u'BLF', u'CLIFFS': u'CLFS', u'FORK': u'FRK', u'STA': u'STA', u'KEYS': u'KYS', u'STN': u'STA', \
u'RANCH': u'RNCH', u'FORG': u'FRG', u'REST': u'RST', u'FORD': u'FRD', u'FRWAY': u'FWY', u'CRSSNG': u'XING', u'CNTR': u'CTR', \
u'STR': u'ST', u'KNOLL': u'KNL', u'FORT': u'FT', u'BOUL': u'BLVD', u'SQRS': u'SQS', u'HAVEN': u'HVN', u'NCK': u'NCK', \
u'RST': u'RST', u'PIKES': u'PIKE', u'GLENS': u'GLNS', u'SQRE': u'SQ', u'RAPID': u'RPD', u'PKWAY': u'PKWY', u'LK': u'LK', \
u'GARDENS': u'GDNS', u'PIKE': u'PIKE', u'RAD': u'RADL', u'EXTS': u'EXTS', u'BOTTOM': u'BTM', u'STRAV': u'STRA', u'FRRY': u'FRY', \
u'LCKS': u'LCKS', u'CNYN': u'CYN', u'RD': u'RD', u'PRT': u'PRT', u'PRR': u'PR', u'EXTN': u'EXT', u'ROAD': u'RD', u'CRSE': u'CRSE', \
u'CURVE': u'CURV', u'SHOARS': u'SHRS', u'VIA': u'VIA', u'XING': u'XING', u'STREME': u'STRM', u'LAKE': u'LK', u'TRAIL': u'TRL', \
u'RADIAL': u'RADL', u'EXPRESSWAY': u'EXPY', u'JUNCTIONS': u'JCTS', u'CLIFF': u'CLF', u'CNTER': u'CTR', u'PASSAGE': u'PSGE', \
u'TRAFFICWAY': u'TRFY', u'MEADOWS': u'MDWS', u'HARBORS': u'HBRS', u'MOUNTAIN': u'MTN', u'GREENS': u'GRNS', u'ANNX': u'ANX', \
u'CEN': u'CTR', u'PKY': u'PKWY', u'FALLS': u'FLS', u'STRVN': u'STRA', u'BRNCH': u'BR', u'HILL': u'HL', u'VILLAGE': u'VLG', \
u'PLNS': u'PLNS', u'SHR': u'SHR', u'MISSN': u'MSN', u'STRAVN': u'STRA', u'PLAZA': u'PLZ', u'EXPY': u'EXPY', u'MOTORWAY': u'MTWY', \
u'BOTTM': u'BTM', u'SHRS': u'SHRS', u'HWAY': u'HWY', u'CREST': u'CRST', u'HIGHWAY': u'HWY', u'GLEN': u'GLN', u'SHORES': u'SHRS', \
u'MOUNTIN': u'MTN', u'CRES': u'CRES', u'CANYON': u'CYN', u'LOOP': u'LOOP', u'FRKS': u'FRKS', u'BTM': u'BTM', u'CENTERS': u'CTRS', \
u'COURT': u'CT', u'ISS': u'ISS', u'SPRING': u'SPG', u'TUNL': u'TUNL', u'HARBR': u'HBR', u'COURTS': u'CTS', u'LANE': u'LN', \
u'LAND': u'LAND', u'JCTION': u'JCT', u'EXPR': u'EXPY', u'STREETS': u'STS', u'EXPW': u'EXPY', u'LAKES': u'LKS', u'CAUSEWAY': u'CSWY', \
u'VILLIAGE': u'VLG', u'GATEWY': u'GTWY', u'VISTA': u'VIS', u'FRG': u'FRG', u'MOUNTAINS': u'MTNS', u'FRK': u'FRK', u'CLF': u'CLF',\
u'CLB': u'CLB', u'SKYWAY': u'SKWY', u'FRT': u'FT', u'FRY': u'FRY', u'BOULV': u'BLVD', u'ISLNDS': u'ISS', u'HVN': u'HVN', \
u'KEY': u'KY', u'KY': u'KY', u'FLTS': u'FLTS', u'BRIDGE': u'BRG', u'DL': u'DL', u'DM': u'DM', u'EXTENSION': u'EXT', u'LODG': u'LDG', \
u'ESTATES': u'ESTS', u'ISLND': u'IS', u'DV': u'DV', u'PATH': u'PATH', u'DR': u'DR', u'HIGHWY': u'HWY', u'VALLEYS': u'VLYS', \
u'CAMP': u'CP', u'RPD': u'RPD', u'LOOPS': u'LOOP', u'RAPIDS': u'RPDS', u'HOLW': u'HOLW', u'RNCHS': u'RNCH', u'HOLLOW': u'HOLW', \
u'VALLY': u'VLY', u'MILL': u'ML', u'STRVNUE': u'STRA', u'ANNEX': u'ANX', u'PNES': u'PNES', u'TUNNL': u'TUNL', u'ISLES': u'ISLE', \
u'LGT': u'LGT', u'MEADOW': u'MDW', u'TRAILS': u'TRL', u'EXT': u'EXT', u'STREET': u'ST', u'WELLS': u'WLS', u'EXP': u'EXPY', \
u'BLVD': u'BLVD', u'WY': u'WAY', u'CIRCLES': u'CIRS', u'RIV': u'RIV', u'GRDEN': u'GDN', u'TUNNELS': u'TUNL', u'PATHS': u'PATH', \
u'KNL': u'KNL', u'PARK': u'PARK', u'VILLAGES': u'VLGS', u'PARKS': u'PARK', u'TRACKS': u'TRAK', u'BLUF': u'BLF', u'PASS': u'PASS', \
u'BND': u'BND', u'GRDNS': u'GDNS', u'RDGS': u'RDGS', u'LNDG': u'LNDG', u'LANDING': u'LNDG', u'RDGE': u'RDG', u'CIRCLE': u'CIR', \
u'LIGHT': u'LGT', u'COMMONS': u'CMNS', u'VLYS': u'VLYS', u'FREEWAY': u'FWY', u'SHORE': u'SHR', u'CRK': u'CRK', u'PORT': u'PRT', \
u'SPNGS': u'SPGS', u'PR': u'PR', u'LDG': u'LDG', u'PT': u'PT', u'FIELDS': u'FLDS', u'DRIV': u'DR', u'MALL': u'MALL', \
u'BYPASS': u'BYP', u'PL': u'PL', u'MEWS': u'MEWS', u'DIVIDE': u'DV', u'CLUB': u'CLB', u'VILL': u'VLG', u'TRLRS': u'TRLR', \
u'LODGE': u'LDG', u'ANEX': u'ANX', u'TRAILER': u'TRLR', u'UNDERPASS': u'UPAS', u'NECK': u'NCK', u'TRACE': u'TRCE', u'TRACK': u'TRAK', \
u'FRST': u'FRST', u'STRT': u'ST', u'RPDS': u'RPDS', u'STRM': u'STRM', u'STRA': u'STRA', u'ANX': u'ANX', u'LCK': u'LCK', u'COR': u'COR', \
u'JUNCTION': u'JCT', u'STREAM': u'STRM', u'DVD': u'DV', u'HARB': u'HBR', u'PRK': u'PARK', u'RIVR': u'RIV', u'OVAL': u'OVAL', \
u'VIST': u'VIS', u'MANOR': u'MNR', u'TUNNEL': u'TUNL', u'GTWAY': u'GTWY', u'PKWY': u'PKWY', u'AVENU': u'AVE', u'JUNCTON': u'JCT', \
u'SUMMIT': u'SMT', u'HWY': u'HWY', u'MTIN': u'MTN', u'TRACES': u'TRCE', u'TERRACE': u'TER', u'ORCHARD': u'ORCH', u'CENTRE': u'CTR', \
u'LOCK': u'LCK', u'COVES': u'CVS', u'FIELD': u'FLD', u'WAY': u'WAY', u'STATN': u'STA', u'CP': u'CP', u'GROV': u'GRV', u'CV': u'CV', \
u'CT': u'CT', u'LNDNG': u'LNDG', u'RUN': u'RUN', u'PLZ': u'PLZ', u'TRAK': u'TRAK', u'RUE': u'RUE', u'LOCKS': u'LCKS', u'PLN': u'PLN', \
u'MNTN': u'MTN', u'FRWY': u'FWY', u'DIV': u'DV', u'KNOLLS': u'KNLS', u'LIGHTS': u'LGTS', u'CRCLE': u'CIR', u'HIWY': u'HWY', \
u'TERR': u'TER', u'JCT': u'JCT', u'INLT': u'INLT', u'IS': u'IS', u'BROOK': u'BRK', u'BROOKS': u'BRKS', u'MTN': u'MTN', u'CIRCL': u'CIR', \
u'VW': u'VW', u'FLATS': u'FLTS', u'PINE': u'PNE', u'ARC': u'ARC', u'LDGE': u'LDG', u'FREEWY': u'FWY', u'HILLS': u'HLS', u'SHLS': u'SHLS',\
u'BOT': u'BTM', u'BRDGE': u'BRG', u'DRV': u'DR', u'FWY': u'FWY', u'BR': u'BR', u'BCH': u'BCH', u'FORKS': u'FRKS', u'HIWAY': u'HWY', \
u'VL': u'VL', u'HBR': u'HBR', u'TURNPK': u'TPKE', u'CTR': u'CTR', u'CENT': u'CTR', u'CROSSROADS': u'XRDS', u'RVR': u'RIV', \
u'HOLWS': u'HOLW', u'PRAIRIE': u'PR', u'BRANCH': u'BR', u'VALLEY': u'VLY', u'ALLY': u'ALY', u'GROVE': u'GRV', u'CLFS': u'CLFS', \
u'RIDGES': u'RDGS', u'PORTS': u'PRTS', u'VILLAG': u'VLG', u'BYPA': u'BYP', u'VIEWS': u'VWS', u'HARBOR': u'HBR', u'SQR': u'SQ', \
u'SQU': u'SQ', u'BYPS': u'BYP', u'FORDS': u'FRDS', u'MANORS': u'MNRS', u'ISLE': u'ISLE', u'CRCL': u'CIR', u'BURG': u'BG', \
u'HLLW': u'HOLW', u'GARDEN': u'GDN', u'FLS': u'FLS', u'FLT': u'FLT', u'HT': u'HTS', u'HL': u'HL', u'AVENUE': u'AVE', u'FLD': u'FLD', \
u'GTWY': u'GTWY', u'CENTER': u'CTR', u'VIS': u'VIS', u'MNR': u'MNR', u'MNT': u'MT', u'PLAINS': u'PLNS', u'JUNCTN': u'JCT', \
u'PTS': u'PTS', u'ROW': u'ROW', u'FORGES': u'FRGS', u'BOULEVARD': u'BLVD', u'TRL': u'TRL', u'COURSE': u'CRSE', u'TRKS': u'TRAK', \
u'CAPE': u'CPE', u'SHOAR': u'SHR', u'VIADUCT': u'VIA', u'AVN': u'AVE', u'UN': u'UN', u'HTS': u'HTS', u'SHOAL': u'SHL', \
u'CROSSING': u'XING', u'AVE': u'AVE', u'ROUTE': u'RTE', u'FLDS': u'FLDS', u'VLGS': u'VLGS', u'AVNUE': u'AVE', u'ESTS': u'ESTS', \
u'FORGE': u'FRG', u'STRAVENUE': u'STRA', u'MNTNS': u'MTNS', u'AVEN': u'AVE', u'VLLY': u'VLY', u'VSTA': u'VIS', u'WALKS': u'WALK', \
u'TER': u'TER', u'PRTS': u'PRTS', u'RDS': u'RDS', u'MILLS': u'MLS', u'RDG': u'RDG', u'KNLS': u'KNLS', u'CORS': u'CORS', \
u'CANYN': u'CYN', u'CROSSROAD': u'XRD', u'SPURS': u'SPUR', u'VILLE': u'VL', u'VILLG': u'VLG', u'WAYS': u'WAYS', u'ISLAND': u'IS', \
u'SUMIT': u'SMT', u'MDWS': u'MDWS', u'CIRC': u'CIR', u'BRK': u'BRK', u'BRG': u'BRG', u'DALE': u'DL', u'TRNPK': u'TPKE', u'WALK': u'WALK', \
u'HRBOR': u'HBR', u'WALL': u'WALL', u'BLUFFS': u'BLFS', u'DRIVE': u'DR', u'PLZA': u'PLZ', u'CIR': u'CIR', u'RANCHES': u'RNCH', \
u'PARKWAY': u'PKWY', u'SPNG': u'SPG', u'EXTNSN': u'EXT', u'ARCADE': u'ARC', u'DAM': u'DM', u'WELL': u'WL', u'ALLEY': u'ALY', \
u'LKS': u'LKS', u'ALLEE': u'ALY', u'POINTS': u'PTS', u'FOREST': u'FRST', u'ORCH': u'ORCH', u'CORNERS': u'CORS', u'EST': u'EST', \
u'STRAVEN': u'STRA', u'SHOALS': u'SHLS', u'RNCH': u'RNCH', u'HOLLOWS': u'HOLW', u'AV': u'AVE', u'SQUARES': u'SQS', u'GDNS': u'GDNS', \
u'SPGS': u'SPGS', u'VST': u'VIS', u'CAUSWA': u'CSWY', u'GATEWAY': u'GTWY', u'UNIONS': u'UNS', u'GATWAY': u'GTWY'}



# Extras
street_type_replacement_dict['PK'] = 'PIKE'
street_type_replacement_dict['STREE'] = 'ST'
street_type_replacement_dict['CR'] = 'CIR'
street_type_replacement_dict['PLACE'] = 'PL'
street_type_replacement_dict['QT'] = 'CT'
street_type_replacement_dict['STS'] = 'ST'
#street_type_replacement_dict[''] = ''


# Upper case the string before testing
street_direction_replacement_dict = {'NORTH': 'N', 'SOUTH': 'S', 'EAST': 'E', 'WEST': 'W', 'NORTHEAST': 'NE', 'NORTHWEST': 'NW', \
    'SOUTHEAST': 'SE', 'SOUTHWEST': 'SW', 'SO': 'S', 'WWEST': 'W', }



# From table C2 on pg 72 of http://pe.usps.gov/cpim/ftp/pubs/Pub28/pub28.pdf
usps_unit_designators = {'LOWER': 'LOWR', 'OFFICE': 'OFC', 'FLR': 'FL', 'STOP': 'STOP', 'HANGER': 'HNGR', \
    'LOT': 'LOT', 'SUITE': 'STE', 'REAR': 'REAR', 'PENTHOUSE': 'PH', 'ROOM': 'RM', 'SPACE': 'SPC', \
    'UNIT': 'UNIT', 'FRONT': 'FRNT', 'LOBBY': 'LBBY', 'APARTMENT': 'APT', 'FLOOR': 'FL', 'DEPARTMENT': 'DEPT', \
    'SLIP': 'SLIP', 'BASEMENT': 'BSMT', 'PIER': 'PIER', 'TRAILER': 'TRLR', 'BUILDING': 'BLDG', 'UPPER': 'UPPR', \
    'SUTIE': 'STE', 'KEY': 'KEY', 'SIDE': 'SIDE'}

# Add custom
usps_unit_designators['FLR'] = 'FL'

usps_unit_designators['NO'] = '#'
usps_unit_designators['NUMBER'] = '#'
usps_unit_designators['CONDO'] = '#'

usps_unit_designators['SUTIE'] = 'STE'
usps_unit_designators['SIOTE'] = 'STE'
usps_unit_designators['SITE'] = 'STE'
usps_unit_designators['STE:'] = 'STE'
usps_unit_designators['SUTE'] = 'STE'
usps_unit_designators['SUIT'] = 'STE'


usps_unit_designators['UNTI'] = 'UNIT'
usps_unit_designators['UNITE'] = 'UNIT'
usps_unit_designators['UNIY'] = 'UNIT'
usps_unit_designators['UNITE'] = 'UNIT'
usps_unit_designators['UNIT, UNIT'] = 'UNIT'


usps_unit_designators['APT. APT'] = 'APT'
usps_unit_designators['APPT'] = 'APT'
#usps_unit_designators[''] = ''



fields_to_strip_periods = ['StreetNamePostType', 'StreetNamePreDirectional', 'AddressNumberSuffix', 'StreetNamePostModifier', \
    'StreetNamePostDirectional', 'OccupancyType', 'SubaddressType', 'SecondStreetNamePostType', 'USPSBoxGroupType']


def standardize_us_address(mailing_address):

    """
    This function takes an text address (street address, city, state, zip), tokenizes it with the usaddress library,
    and runs basic search and replace to help standardize the address

    """


    try:

        usaddress_address = usaddress.tag(mailing_address)

        #print 'usaddress addy:', usaddress_address

        address_dict = dict(usaddress_address[0])

        address_type = usaddress_address[1]
        address_dict['address_type'] = address_type
        address_dict['original_address'] = mailing_address

        # Make sure we're using state abbreviation instead of full state name
        if 'StateName' in address_dict and address_dict['StateName'] in state_replacement_dict:
            address_dict['StateName'] = state_replacement_dict[address_dict['StateName']]


        # Remove trailing '.' from any abbreviations
        for field in fields_to_strip_periods:
            if field in address_dict:
                address_dict[field] = address_dict[field].strip('.')


        # Use standard abbreviated for street direction (N instead of North)
        if 'StreetNamePreDirectional' in address_dict:
            address_dict['StreetNamePreDirectional'] = address_dict['StreetNamePreDirectional'].strip().replace(' ', '').replace('.', '')
            if address_dict['StreetNamePreDirectional'] in street_direction_replacement_dict:
                address_dict['StreetNamePreDirectional'] = street_direction_replacement_dict[address_dict['StreetNamePreDirectional']]
        
        if 'StreetNamePostDirectional' in address_dict:
            address_dict['StreetNamePostDirectional'] = address_dict['StreetNamePostDirectional'].strip().replace(' ', '').replace('.', '')
            if address_dict['StreetNamePostDirectional'] in street_direction_replacement_dict:
                address_dict['StreetNamePostDirectional'] = street_direction_replacement_dict[address_dict['StreetNamePostDirectional']]

        if 'SecondStreetNamePostDirectional' in address_dict:
            address_dict['SecondStreetNamePostDirectional'] = address_dict['SecondStreetNamePostDirectional'].strip().replace(' ', '').replace('.', '')
            if address_dict['SecondStreetNamePostDirectional'] in street_direction_replacement_dict:
                address_dict['SecondStreetNamePostDirectional'] = street_direction_replacement_dict[address_dict['SecondStreetNamePostDirectional']]




        # Use standard abbreviated for street type (Rd instead of Road)
        if 'StreetNamePostType' in address_dict and address_dict['StreetNamePostType'].strip() in street_type_replacement_dict:
                address_dict['StreetNamePostType'] = street_type_replacement_dict[address_dict['StreetNamePostType'].strip()]

        if 'SecondStreetNamePostType' in address_dict and address_dict['SecondStreetNamePostType'].strip() in street_type_replacement_dict:
                address_dict['SecondStreetNamePostType'] = street_type_replacement_dict[address_dict['SecondStreetNamePostType'].strip()]

        if 'USPSBoxGroupType' in address_dict and address_dict['USPSBoxGroupType'].strip() in street_type_replacement_dict:
                address_dict['USPSBoxGroupType'] = street_type_replacement_dict[address_dict['USPSBoxGroupType'].strip()]




        # Standardize unit types
        if 'OccupancyType' in address_dict and address_dict['OccupancyType'].strip() in usps_unit_designators:
                address_dict['OccupancyType'] = usps_unit_designators[address_dict['OccupancyType'].strip()]

        if 'SubaddressType' in address_dict and address_dict['SubaddressType'].strip() in usps_unit_designators:
                address_dict['SubaddressType'] = usps_unit_designators[address_dict['SubaddressType'].strip()]




        # Remove preceiding '#' from OccupancyIdentifier
        if 'OccupancyIdentifier' in address_dict and address_dict['OccupancyIdentifier'][0] == '#':
            address_dict['OccupancyIdentifier'] = address_dict['OccupancyIdentifier'].strip('#').strip()

            # If OccupancyType is not set, and OccupancyIdentifier is set, and OccupancyIdentifier starts with '#' 
            # then make '#' the OccupancyType
            if 'OccupancyType' not in address_dict:
                address_dict['OccupancyType'] = '#'


        # If USPSBoxType is set, just make it 'PO BOX'
        if 'USPSBoxType' in address_dict:
            address_dict['USPSBoxType'] = 'PO BOX'


        # Only connect multiple streets with '&' 
        if 'IntersectionSeparator' in address_dict and address_dict['IntersectionSeparator'] == 'AND':
            address_dict['IntersectionSeparator'] = '&'


        # Only use first 5 digits in zip code, don't care about extended
        if 'ZipCode' in address_dict and len(address_dict['ZipCode']) > 5:
            address_dict['ZipCode'] = ''.join([i for i in address_dict['ZipCode'] if i.isdigit()])[:5]


        # Clean up state name. Remove ', DE' if length is 6 and last three == ', DE'
        if 'StateName' in address_dict and len(address_dict['StateName']) == 6 and address_dict['StateName'][2:] == ', DE':
            address_dict['StateName'] = address_dict['StateName'][:2]


        return address_dict


    except Exception as e:

        print 'usaddress ERROR:'
        print e

        return e






