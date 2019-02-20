import json

valid_values = {
    "attribute": ["info", "sitelinks", "aliases", "labels", "descriptions", "claims", "datatype"],
    "entity": ["item", "property", "lexeme", "form", "sense"],
    "language": [
        "aa",
        "ab",
        "abs",
        "ace",
        "ady",
        "ady-cyrl",
        "aeb",
        "aeb-arab",
        "aeb-latn",
        "af",
        "ak",
        "aln",
        "als",
        "am",
        "an",
        "ang",
        "anp",
        "ar",
        "arc",
        "arn",
        "arq",
        "ary",
        "arz",
        "as",
        "ase",
        "ast",
        "atj",
        "av",
        "avk",
        "awa",
        "ay",
        "az",
        "azb",
        "ba",
        "ban",
        "bar",
        "bat-smg",
        "bbc",
        "bbc-latn",
        "bcc",
        "bcl",
        "be",
        "be-tarask",
        "be-x-old",
        "bg",
        "bgn",
        "bh",
        "bho",
        "bi",
        "bjn",
        "bm",
        "bn",
        "bo",
        "bpy",
        "bqi",
        "br",
        "brh",
        "bs",
        "btm",
        "bto",
        "bug",
        "bxr",
        "ca",
        "cbk-zam",
        "cdo",
        "ce",
        "ceb",
        "ch",
        "cho",
        "chr",
        "chy",
        "ckb",
        "co",
        "cps",
        "cr",
        "crh",
        "crh-cyrl",
        "crh-latn",
        "cs",
        "csb",
        "cu",
        "cv",
        "cy",
        "da",
        "de",
        "de-at",
        "de-ch",
        "de-formal",
        "din",
        "diq",
        "dsb",
        "dtp",
        "dty",
        "dv",
        "dz",
        "ee",
        "egl",
        "el",
        "eml",
        "en",
        "en-ca",
        "en-gb",
        "eo",
        "es",
        "es-419",
        "es-formal",
        "et",
        "eu",
        "ext",
        "fa",
        "ff",
        "fi",
        "fit",
        "fiu-vro",
        "fj",
        "fo",
        "fr",
        "frc",
        "frp",
        "frr",
        "fur",
        "fy",
        "ga",
        "gag",
        "gan",
        "gan-hans",
        "gan-hant",
        "gcr",
        "gd",
        "gl",
        "glk",
        "gn",
        "gom",
        "gom-deva",
        "gom-latn",
        "gor",
        "got",
        "grc",
        "gsw",
        "gu",
        "gv",
        "ha",
        "hak",
        "haw",
        "he",
        "hi",
        "hif",
        "hif-latn",
        "hil",
        "ho",
        "hr",
        "hrx",
        "hsb",
        "ht",
        "hu",
        "hu-formal",
        "hy",
        "hyw",
        "hz",
        "ia",
        "id",
        "ie",
        "ig",
        "ii",
        "ik",
        "ike-cans",
        "ike-latn",
        "ilo",
        "inh",
        "io",
        "is",
        "it",
        "iu",
        "ja",
        "jam",
        "jbo",
        "jut",
        "jv",
        "ka",
        "kaa",
        "kab",
        "kbd",
        "kbd-cyrl",
        "kbp",
        "kea",
        "kg",
        "khw",
        "ki",
        "kiu",
        "kj",
        "kk",
        "kk-arab",
        "kk-cn",
        "kk-cyrl",
        "kk-kz",
        "kk-latn",
        "kk-tr",
        "kl",
        "km",
        "kn",
        "ko",
        "ko-kp",
        "koi",
        "kr",
        "krc",
        "kri",
        "krj",
        "krl",
        "ks",
        "ks-arab",
        "ks-deva",
        "ksh",
        "ku",
        "ku-arab",
        "ku-latn",
        "kum",
        "kv",
        "kw",
        "ky",
        "la",
        "lad",
        "lb",
        "lbe",
        "lez",
        "lfn",
        "lg",
        "li",
        "lij",
        "liv",
        "lki",
        "lmo",
        "ln",
        "lo",
        "loz",
        "lrc",
        "lt",
        "ltg",
        "lus",
        "luz",
        "lv",
        "lzh",
        "lzz",
        "mai",
        "map-bms",
        "mdf",
        "mg",
        "mh",
        "mhr",
        "mi",
        "min",
        "mk",
        "ml",
        "mn",
        "mni",
        "mnw",
        "mo",
        "mr",
        "mrj",
        "ms",
        "mt",
        "mus",
        "mwl",
        "my",
        "myv",
        "mzn",
        "na",
        "nah",
        "nan",
        "nap",
        "nb",
        "nds",
        "nds-nl",
        "ne",
        "new",
        "ng",
        "niu",
        "nl",
        "nl-informal",
        "nn",
        "no",
        "nod",
        "nov",
        "nrm",
        "nso",
        "nv",
        "ny",
        "nys",
        "oc",
        "olo",
        "om",
        "or",
        "os",
        "ota",
        "pa",
        "pag",
        "pam",
        "pap",
        "pcd",
        "pdc",
        "pdt",
        "pfl",
        "pi",
        "pih",
        "pl",
        "pms",
        "pnb",
        "pnt",
        "prg",
        "ps",
        "pt",
        "pt-br",
        "qu",
        "qug",
        "rgn",
        "rif",
        "rm",
        "rmy",
        "rn",
        "ro",
        "roa-rup",
        "roa-tara",
        "ru",
        "rue",
        "rup",
        "ruq",
        "ruq-cyrl",
        "ruq-latn",
        "rw",
        "rwr",
        "sa",
        "sah",
        "sat",
        "sc",
        "scn",
        "sco",
        "sd",
        "sdc",
        "sdh",
        "se",
        "sei",
        "ses",
        "sg",
        "sgs",
        "sh",
        "shi",
        "shi-latn",
        "shi-tfng",
        "shn",
        "shy-latn",
        "si",
        "simple",
        "sje",
        "sk",
        "skr",
        "skr-arab",
        "sl",
        "sli",
        "sm",
        "sma",
        "smj",
        "sn",
        "so",
        "sq",
        "sr",
        "sr-ec",
        "sr-el",
        "srn",
        "srq",
        "ss",
        "st",
        "stq",
        "sty",
        "su",
        "sv",
        "sw",
        "szl",
        "ta",
        "tay",
        "tcy",
        "te",
        "tet",
        "tg",
        "tg-cyrl",
        "tg-latn",
        "th",
        "ti",
        "tk",
        "tl",
        "tly",
        "tn",
        "to",
        "tpi",
        "tr",
        "tru",
        "ts",
        "tt",
        "tt-cyrl",
        "tt-latn",
        "tum",
        "tw",
        "ty",
        "tyv",
        "tzm",
        "udm",
        "ug",
        "ug-arab",
        "ug-latn",
        "uk",
        "ur",
        "uz",
        "uz-cyrl",
        "uz-latn",
        "ve",
        "vec",
        "vep",
        "vi",
        "vls",
        "vmf",
        "vo",
        "vot",
        "vro",
        "wa",
        "war",
        "wo",
        "wuu",
        "xal",
        "xh",
        "xmf",
        "yi",
        "yo",
        "yue",
        "za",
        "zea",
        "zgh",
        "zh",
        "zh-classical",
        "zh-cn",
        "zh-hans",
        "zh-hant",
        "zh-hk",
        "zh-min-nan",
        "zh-mo",
        "zh-my",
        "zh-sg",
        "zh-tw",
        "zh-yue",
        "zu",
    ],
    "rank": ["preferred", "normal", "deprecated"],
    "snak_type": ["value", "novalue", "somevalue"],
}


def validate_value(value, param_name):
    """Raise an exception if the specified value is not an allowed value

    :param value: Value to validate
    :type value: str
    :param param_name: Value domain
    :type param_name: str
    """
    if value not in valid_values[param_name]:
        valid_values_str = json.dumps(valid_values[param_name])
        raise ValueError(
            f'Value "{value}" is not a valid {param_name}. It must be set to one of '
            f"{valid_values_str}"
        )


def validate_snak(value, snak_type):
    """Validate a snak's type and value

    :param value: Value of the snak
    :type value: any
    :param snak_type: Type of the snak (must be one of ``["value", "novalue", "somevalue"]``)
    :type snak_type: str
    """
    validate_value(snak_type, "snak_type")
    if snak_type == "value" and value is None:
        raise ValueError(f"Claim value cannot be None")
    if snak_type != "value" and value is not None:
        raise ValueError(
            f'When using snak_type "{snak_type}, the "value" parameter must be set to None'
        )
