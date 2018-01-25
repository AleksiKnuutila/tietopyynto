from __future__ import unicode_literals

import random
import hashlib

from django.conf import settings

NAMES = ['3_d_man',
'alars',
'aardwolf',
'abdul_alhazred',
'abe_brown',
'abigail_brand',
'abner_jenkins',
'abner_little',
'abominable_snowman',
'abomination',
'abominatrix',
'abraham_cornelius',
'abraxas',
'absalom',
'absorbing_man',
'abyss',
'access',
'achebe',
'achelous',
'achilles',
'acrobat',
'adam_ii',
'adam_warlock',
'adam_x',
'adaptoid',
'administrator',
'adonis',
'adrenazon',
'adri_nital',
'adrian_corbo',
'adrian_toomes',
'adrienne_frost',
'adversary',
'advisor',
'aegis',
'aelfyre_whitemane',
'aero',
'aftershock',
'agamemnon',
'agamotto',
'agatha_harkness',
'aged_genghis',
'agent',
'agent_axis',
'agent_cheesecake',
'agent_x',
'agent_zero',
'aggamon',
'aginar',
'agon',
'agony',
'agron',
'aguja',
'ahab',
'ahmet_abdol',
'ahura',
'air_walker',
'airborne',
'aireo',
'airstrike',
'ajak',
'ajax',
'ajaxis',
'akasha',
'akhenaten',
'al_mackenzie',
'alaris',
'albert',
'albino',
'albion',
'alchemy',
'alcmena',
'aldebron',
'aleksander_lukin',
'aleksei_sytsevich',
'aleta_ogord',
'alex',
'alex_hayden',
'alex_power',
'alex_wilder',
'alexander_bont',
'alexander_goodwin_pierce',
'alexander_lexington',
'alexander_summers',
'alfie_omeggan',
'algrim_the_strong',
'alibar',
'alicia_masters',
'alistair_smythe',
'alistaire_stuart',
'aliyah_bishop',
'alkhema',
'all_american',
'allato',
'allison_blaire',
'alpha_ray',
'alpha_the_ultimate_mutant',
'alyosha_kravinoff',
'alysande_stuart',
'alyssa_moy',
'amahl_farouk',
'amalgam',
'amanda_sefton',
'amatsu_mikaboshi',
'amazon',
'amber_hunt',
'amelia_voght',
'amergin',
'american_ace',
'american_dream',
'american_eagle',
'american_samurai',
'americop',
'ameridroid',
'amiko_kobayashi',
'amina_synge',
'aminedi',
'ammo',
'amphibian',
'amphibion',
'amphibius',
'amun',
'anaconda',
'anais',
'analyzer',
'anarchist',
'ancient_one',
'andreas_von_strucker',
'andrew_chord',
'andrew_gervais',
'android_man',
'andromeda',
'anelle',
'angar_the_screamer',
'angel',
'angel_dust',
'angel_face',
'angel_salvadore',
'angela_cairn',
'angela_del_toro',
'angelica_jones',
'angelo_unuscione',
'angler',
'ani_mator',
'animus',
'ankhi',
'annalee',
'anne_marie_cortez',
'annex',
'annie_ghazikhanian',
'annihilus',
'anole',
'anomalito',
'anomaloco',
'anomaly',
'answer',
'ant_man',
'anthropomorpho',
'anti_cap',
'anti_phoenix_force',
'anti_venom',
'anti_vision',
'antimatter',
'antiphon_the_overseer',
'antonio',
'anubis',
'anvil',
'anything',
'apache_kid',
'apalla',
'ape',
'ape_man',
'ape_x',
'apocalypse',
'apollo',
'apryll',
'aquarian',
'aquarius',
'aqueduct',
'arabian_knight',
'arachne',
'aragorn',
'araki',
'aralune',
'arana',
'arc',
'arcade',
'arcademan',
'arcanna',
'archangel',
'archenemy',
'archer',
'archie_corrigan',
'archimage',
'architect',
'arclight',
'arcturus_rann',
'ardina',
'ardroman',
'arena',
'ares',
'argo',
'argus',
'ariann',
'arides',
'ariel',
'aries',
'arishem_the_judge',
'arize',
'arizona_annie',
'arkady_rossovich',
'arkon',
'arkus',
'arlette_truffaut',
'arlok',
'armadillo',
'armageddon',
'armand_martel',
'armor',
'armory',
'arnim_zola',
'arno_stark',
'arranger',
'arsenal',
'arsenic',
'artemis',
'arthur_parks',
'artie',
'artie_maddicks',
'arturo_falcones',
'asbestos_lady',
'asbestos_man',
'ashcan',
'asmodeus',
'asp',
'assassin',
'asteroth',
'astra',
'astrid_bloom',
'astron',
'astronomer',
'asylum',
'atalanta',
'atalon',
'athena',
'atlas',
'atleza',
'atom_bob',
'atom_smasher',
'att_lass',
'attuma',
'atum',
'aunt_may_parker',
'auntie_freeze',
'auric',
'aurora',
'authority',
'autolycus',
'avalanche',
'avarrish',
'awesome_android',
'axum',
'azazel',
'baal',
'balder',
'balor',
'balthakk',
'bandit',
'banshee',
'bantam',
'baphomet',
'barbarus',
'barnacle',
'baron_blood',
'baron_brimstone',
'baron_macabre',
'baron_mordo',
'baron_samedi',
'baron_strucker',
'baron_von_blitzschlag',
'baron_zemo',
'baroness_blood',
'barracuda',
'bart_hamilton',
'base',
'basil_sandhurst',
'basilisk',
'bast',
'bastion',
'batragon',
'batroc_the_leaper',
'battering_ram',
'battleaxe',
'battlestar',
'battletide',
'batwing',
'beast',
'beautiful_dreamer',
'bedlam',
'bedlam_ii',
'beetle',
'beetle_ii',
'behemoth',
'bela',
'belasco',
'belathauzer',
'bella_donna',
'ben_parker',
'ben_reilly',
'ben_urich',
'benazir_kaur',
'benedict_kine',
'bengal',
'benjamin_jacob_grimm',
'bennet_du_paris',
'benny_beckley',
'bentley_wittman',
'bereet',
'berzerker',
'bes',
'beta_ray_bill',
'bethany_cabe',
'betty_brant',
'betty_brant_leeds',
'betty_ross_banner',
'bevatron',
'beyonder',
'bi_beast',
'bible_john',
'big_bertha',
'big_man',
'big_wheel',
'bill_foster',
'binary',
'bird_brain',
'bird_man',
'bishop',
'bison',
'bizarnage',
'black_bolt',
'black_box',
'black_cat',
'black_crow',
'black_death',
'black_dragon',
'black_fox',
'black_goliath',
'black_jack_tarr',
'black_king',
'black_knight',
'black_lama',
'black_mamba',
'black_marvel',
'black_panther',
'black_queen',
'black_talon',
'black_tarantula',
'black_tom_cassidy',
'black_widow',
'blackbird',
'blackheart',
'blackheath',
'blacklash',
'blackout',
'blackwing',
'blackwulf',
'blade',
'blaquesmith',
'blastaar',
'blaze',
'blazing_skull',
'blind_faith',
'blind_justice',
'blindside',
'blindspot',
'bling',
'blink',
'blistik',
'blitziana',
'blitzkrieger',
'blizzard',
'blizzard_ii',
'blob',
'blockbuster',
'bloke',
'blonde_phantom',
'blood_brothers',
'blood_rose',
'blood_spider',
'bloodaxe',
'bloodhawk',
'bloodlust',
'bloodlust_ii',
'bloodscream',
'bloodshed',
'bloodsport',
'bloodstorm',
'bloodtide',
'bloodwraith',
'blowhard',
'blue_bullet',
'blue_diamond',
'blue_marvel',
'blue_shield',
'blue_streak',
'blur',
'bob',
'bob_diamond',
'bobster',
'bogeyman',
'bombshell',
'boneyard',
'bonita_juarez',
'boobytrap',
'book',
'boom_boom',
'boom_boy',
'boomer',
'boomerang',
'boomslang',
'boost',
'bora',
'bounty',
'bounty_hunter',
'bova',
'box',
'box_iv',
'brain_cell',
'brain_drain',
'brain_child',
'brainchild',
'bram_velsing',
'brass',
'bres',
'brian_braddock',
'brian_falsworth',
'brigade',
'briquette',
'brother_nature',
'brother_tode',
'brother_voodoo',
'brothers_grimm',
'bruiser',
'brunnhilda',
'brutacus',
'brute_i',
'brute_ii',
'brute_iii',
'brynocki',
'bucky',
'bucky_iii',
'bug',
'bulldozer',
'bullet',
'bullseye',
'burner',
'burstarr',
'bushman',
'bushmaster',
'bushwacker',
'butterball',
'buzz',
'buzzard',
'byrrah',
'caber',
'cable',
'cadaver',
'cagliostro',
'caiera',
'caiman',
'cain',
'cain_marko',
'caleb_alexander',
'caliban',
'callisto',
'calvin_rankin',
'calypso',
'cameron_hodge',
'canasta',
'cancer',
'candra',
'cannonball',
'cannonball_i',
'cap_n_hawk',
'caprice',
'capricorn',
'captain_america',
'captain_atlas',
'captain_barracuda',
'captain_britain',
'captain_fate',
'captain_germany',
'captain_marvel',
'captain_omen',
'captain_savage',
'captain_uk',
'captain_ultra',
'captain_universe',
'captain_wings',
'captain_zero',
'cardiac',
'cardinal',
'caregiver',
'caretaker',
'carl_crusher_creel',
'carlos_lobo',
'carmella_unuscione',
'carmilla_black',
'carnage',
'carnivore',
'carolyn_parmenter',
'carolyn_trainer',
'carrie_alexander',
'carrion',
'carter_ghazikhanian',
'cassandra_nova',
'cassie_lang',
'cassiopea',
'cat',
'cat_man',
'catiana',
'cayman',
'cecelia_reyes',
'cecilia_reyes',
'celestial_madonna',
'centennial',
'centurion',
'centurious',
'centurius',
'cerberus',
'cerebra',
'cerise',
'cessily_kincaid',
'cethlann',
'chod',
'chaka',
'challenger',
'chamber',
'chameleon',
'champion_of_the_universe',
'chan_luichow',
'chance',
'changeling',
'chaos',
'charcoal',
'charles_xavier',
'charlie_27',
'charon',
'chase_stein',
'cheetah',
'chemistro',
'chen_l',
'chi_demon',
'chief_examiner',
'chimera',
'chloe_tran',
'choice',
'chondu_the_mystic',
'christopher_summers',
'chrome',
'chronos',
'chthon',
'chtylok',
'citizen_v',
'claire_voyant',
'claudette_st_croix',
'clea',
'clearcut',
'cletus_kasady',
'clint_barton',
'clive',
'cloak',
'cloud',
'cloud_9',
'clown',
'coach',
'coachwhip',
'cobalt_man',
'cobra',
'cody_mushumanski_gun_man',
'cold_war',
'coldblood',
'coldfire',
'collective_man',
'collector',
'colleen_wing',
'colonel',
'colonel_america',
'colossus',
'comet',
'comet_man',
'commander_kraken',
'commando',
'conan_the_barbarian',
'condor',
'conquer_lord',
'conquest',
'conquistador',
'conrad_josten',
'constrictor',
'contemplator',
'contessa',
'contrary',
'controller',
'copperhead',
'copycat',
'coral',
'cordelia_frost',
'cornelius_van_lunt',
'corona',
'corruptor',
'corsair',
'cottonmouth',
'count_abyss',
'count_nefaria',
'courier',
'cowgirl',
'crazy_eight',
'crime_master',
'crime_buster',
'crimebuster',
'crimson',
'crimson_cavalier',
'crimson_commando',
'crimson_cowl',
'crimson_craig',
'crimson_daffodil',
'crimson_dynamo',
'crimson_dynamo_v',
'crimson_and_the_raven',
'crippler',
'crooked_man',
'crossbones',
'crossfire',
'crown',
'crucible',
'crusader',
'crusher',
'crystal',
'curtis_connors',
'cutthroat',
'cybele',
'cybelle',
'cyber',
'cyborg_x',
'cyclone',
'cyclops',
'cypher',
'dken',
'dspayre',
'd_man',
'dj',
'dagger',
'daisy_johnson',
'dakimh_the_enchanter',
'dakota_north',
'damballah',
'damion_hellstrom',
'damon_dran',
'dan_ketch',
'danger',
'daniel_rand',
'danielle_moonstar',
'dansen_macabre',
'danvers_carol',
'daredevil',
'dark_angel',
'dark_beast',
'dark_phoenix',
'dark_crawler',
'darkdevil',
'darkhawk',
'darkoth',
'darkstar',
'david_cannon',
'daytripper',
'dazzler',
'deacon_frost',
'dead_girl',
'deadhead',
'deadly_ernest',
'deadpool',
'death',
'death_adder',
'deaths_head',
'deaths_head_ii',
'death_stalker',
'deathbird',
'deathlok',
'deathstroke',
'deathurge',
'deathwatch',
'deborah_ritter',
'debra_whitman',
'decay',
'decay_ii',
'defensor',
'delilah',
'delphi',
'delphine_courtney',
'dementia',
'demiurge',
'demogoblin',
'demogorge_the_god_eater',
'demolition_man',
'derrick_slegers_speed',
'desmond_pitt',
'destiny',
'destroyer',
'destroyer_of_demons',
'devastator',
'devil_dinosaur',
'devil_hunter_gabriel',
'devil_slayer',
'devos_the_devastator',
'diablo',
'diamanda_nero',
'diamond_lil',
'diamondback',
'diamondhead',
'digitek',
'dionysus',
'dirtnap',
'discus',
'dittomaster',
'dmitri_bukharin',
'dmitri_smerdyakov',
'doc_samson',
'doctor_anthony_droom',
'doctor_arthur_nagan',
'doctor_bong',
'doctor_demonicus',
'doctor_doom',
'doctor_dorcas',
'doctor_droom',
'doctor_druid',
'doctor_faustus',
'doctor_glitternight',
'doctor_leery',
'doctor_minerva',
'doctor_octopus',
'doctor_spectrum',
'doctor_strange',
'doctor_sun',
'domina',
'dominic_fortune',
'dominic_petros',
'domino',
'dominus',
'domo',
'don_fortunato',
'donald_donny_gill',
'donald_pierce',
'donald_ritter',
'doop',
'doorman',
'doppelganger',
'doppleganger',
'dorma',
'dormamm',
'double_helix',
'doug_ramsey',
'doug_and_jerry',
'dougboy',
'doughboy',
'douglas_birely',
'douglas_ramsey',
'douglock',
'dr_john_grey',
'dr_lemuel_dorcas',
'dr_marla_jameson',
'dr_otto_octavius',
'dracula',
'dragon_lord',
'dragon_man',
'dragon_of_the_moon',
'dragoness',
'dragonfly',
'dragonwing',
'drax_the_destroyer',
'dreadknight',
'dreadnought',
'dream_weaver',
'dreaming_celestial',
'dreamqueen',
'dredmund_druid',
'dromedan',
'druid',
'druig',
'dum_dum_dugan',
'dusk',
'dust',
'dweller_in_darkness',
'dyna_mite',
'earth_lord',
'earthquake',
'ebenezer_laughton',
'ebon_seeker',
'echo',
'ecstasy',
'ectokid',
'eddie_brock',
'edward_ned_buckman',
'edwin_jarvis',
'eel',
'egghead',
'ego_the_living_planet',
'el_aguila',
'el_muerto',
'elaine_grey',
'elathan',
'electric_eve',
'electro',
'electrocute',
'electron',
'eleggua',
'elektra',
'elektra_natchios',
'elektro',
'elf_with_a_gun',
'elfqueen',
'elias_bogan',
'eliminator',
'elixir',
'elizabeth_betsy_braddock',
'elizabeth_twoyoungmen',
'ellie_phimster',
'elsie_dee',
'elven',
'elysius',
'emil_blonsky',
'emma_frost',
'empath',
'empathoid',
'emplate',
'en_sabah_nur',
'enchantress',
'energizer',
'enforcer',
'enigma',
'ent',
'entropic_man',
'eon',
'epoch',
'equilibrius',
'equinox',
'ereshkigal',
'erg',
'eric_slaughter',
'eric_williams',
'eric_the_red',
'erik_josten',
'erik_killmonger',
'erik_magnus_lehnsherr',
'ernst',
'eros',
'esh',
'eson_the_searcher',
'eternal_brain',
'eternity',
'ethan_edwards',
'eugene_judd',
'ev_teel_urizen',
'evangeline_whedon',
'ever',
'everett_thomas',
'everyman',
'evilhawk',
'executioner',
'exodus',
'exploding_man',
'exterminator',
'ezekiel',
'ezekiel_sims',
'ezekiel_stane',
'fabian_cortez',
'fafnir',
'fagin',
'falcon',
'fallen_one',
'famine',
'fan_boy',
'fandral',
'fang',
'fantasia',
'fantastic_four',
'fantomex',
'farallah',
'fasaud',
'fashima',
'fatale',
'fateball',
'father_time',
'fault_zone',
'fearmaster',
'feedback',
'felicia_hardy',
'feline',
'fenris',
'fenris_wolf',
'fer_de_lance',
'feral',
'feron',
'fever_pitch',
'fight_man',
'fin',
'fin_fang_foom',
'firearm',
'firebird',
'firebolt',
'firebrand',
'firefrost',
'firelord',
'firepower',
'firestar',
'fixer',
'fixx',
'flag_smasher',
'flambe',
'flash_thompson',
'flatman',
'flex',
'flint_marko',
'flubber',
'fly',
'flygirl',
'flying_tiger',
'foggy_nelson',
'fontanelle',
'foolkiller',
'forbush_man',
'force',
'forearm',
'foreigner',
'forge',
'forgotten_one',
'foxfire',
'frank_castle',
'frank_drake',
'frank_payne',
'frank_simpson',
'frankensteins_monster',
'frankie_raye',
'frankie_and_victoria',
'franklin_hall',
'franklin_richards',
'franklin_storm',
'freak',
'freak_of_science',
'freakmaster',
'freakshow',
'fred_myers',
'frederick_slade',
'free_spirit',
'freedom_ring',
'frenzy',
'frey',
'frigga',
'frog_man',
'fury',
'fusion',
'futurist',
'g_force',
'gabe_jones',
'gabriel_summers',
'gabriel_the_air_walker',
'gaea',
'gaia',
'gailyn_bailey',
'galactus',
'galaxy_master',
'gambit',
'gammenon_the_gatherer',
'gamora',
'ganymede',
'gardener',
'gargantua',
'gargantus',
'gargouille',
'gargoyle',
'garokk_the_petrified_man',
'garrison_kane',
'gatecrasher',
'gateway',
'gauntlet',
'gavel',
'gaza',
'gazelle',
'gazer',
'geb',
'gee',
'geiger',
'geirrodur',
'gemini',
'general_orwell_taylor',
'genis_vell',
'george_stacy',
'george_tarleton',
'george_washington_bridge',
'georgianna_castleberry',
'gertrude_yorkes',
'ghaur',
'ghost',
'ghost_dancer',
'ghost_girl',
'ghost_maker',
'ghost_rider',
'ghost_rider_2099',
'ghoul',
'giant_man',
'gibbon',
'gibborim',
'gideon',
'gideon_mace',
'giganto',
'gigantus',
'gin_genie',
'gladiator',
'gladiatrix',
'glamor',
'glenn_talbot',
'glitch',
'glob',
'glob_herman',
'gloom',
'glorian',
'goblin_queen',
'goblyn',
'godfrey_calthrop',
'gog',
'goldbug',
'golden_archer',
'golden_girl',
'golden_oldie',
'goldeneye',
'golem',
'goliath',
'gomi',
'googam',
'gorgeous_george',
'gorgilla',
'gorgon',
'gorilla_girl',
'gorilla_man',
'gorr',
'gosamyr',
'grand_director',
'grandmaster',
'grappler',
'grasshopper',
'grasshopper_ii',
'graviton',
'gravity',
'graydon_creed',
'great_gambonnos',
'great_video',
'green_goblin',
'green_goblin_iv',
'greer_grant',
'greer_grant_nelson',
'gregor_shapanka',
'gregory_gideon',
'gremlin',
'grenade',
'grey_gargoyle',
'grey_king',
'griffin',
'grim_hunter',
'grim_reaper',
'grizzly',
'grog_the_god_crusher',
'gronk',
'grotesk',
'groundhog',
'growing_man',
'guardsman',
'guido_carosella',
'gunthar_of_rigel',
'gwen_stacy',
'gypsy_moth',
'herbie',
'hack',
'hag',
'hairbag',
'halflife',
'halloween_jack',
'hamilton_slade',
'hammer_harrison',
'hammer_and_anvil',
'hammerhead',
'hangman',
'hank_mccoy',
'hank_pym',
'hanna_levy',
'hannah_levy',
'hannibal_king',
'harald_jaekelsson',
'hardcase',
'hardcore',
'hardnose',
'hardshell',
'hardwire',
'hargen_the_measurer',
'harmonica',
'harness',
'harold_happy_hogan',
'harold_h_harold',
'harpoon',
'harpy',
'harrier',
'harry_leland',
'harry_osborn',
'hate_monger',
'haven',
'havok',
'hawkeye',
'hawkeye_ii',
'hawkshaw',
'haywire',
'hazard',
'hazmat',
'headknocker',
'headlok',
'heart_attack',
'heather_cameron',
'hebe',
'hecate',
'hector',
'heimdall',
'heinrich_zemo',
'hela',
'helio',
'hellcat',
'helleyes',
'hellfire',
'hellion',
'hellrazor',
'helmut_zemo',
'henry_hank_mccoy',
'henry_peter_gyrich',
'hensley_fargus',
'hephaestus',
'hepzibah',
'her',
'hera',
'herbert_edgar_wyndham',
'hercules',
'herman_schultz',
'hermes',
'hermod',
'hero',
'hero_for_hire',
'herr_kleiser',
'hideko_takata',
'high_evolutionary',
'high_tech',
'hijacker',
'hildegarde',
'him',
'hindsight_lad',
'hippolyta',
'hisako_ichiki',
'hit_maker',
'hitman',
'hobgoblin',
'hobgoblin_ii',
'hoder',
'hogun',
'holly',
'honcho',
'honey_lemon',
'hood',
'hornet',
'horus',
'howard_the_duck',
'hrimhari',
'hub',
'hugh_jones',
'hulk',
'hulk_2099',
'hulkling',
'human_cannonball',
'human_fly',
'human_robot',
'human_top',
'human_top_ii',
'human_torch',
'human_torch_ii',
'humbug',
'humus_sapien',
'huntara',
'hurricane',
'husk',
'hussar',
'hybrid',
'hybrid_ii',
'hyde',
'hydro',
'hydro_man',
'hydron',
'hyperion',
'hyperkind',
'hyperstorm',
'hypnotia',
'hyppokri',
'isaac',
'icarus',
'iceman',
'icemaster',
'idunn',
'iguana',
'ikaris',
'ikonn',
'ikthalon',
'illusion',
'illyana_rasputin',
'immortus',
'impala',
'imperial_hydra',
'impossible_man',
'impulse',
'in_betweener',
'indech',
'indra',
'inertia',
'infamnia',
'infant_terrible',
'infectia',
'inferno',
'infinity',
'interloper',
'invisible_girl',
'invisible_woman',
'inza',
'ion',
'iridia',
'iron_cross',
'iron_fist',
'iron_lad',
'iron_maiden',
'iron_man',
'iron_man_2020',
'iron_monger',
'ironclad',
'isaac_christians',
'isaiah_bradley',
'isbisa',
'isis',
'ivan_kragoff',
'j_jonah_jameson',
'j2',
'jack_flag',
'jack_frost',
'jack_kirby',
'jack_olantern',
'jack_power',
'jack_of_hearts',
'jack_in_the_box',
'jackal',
'jackdaw',
'jackhammer',
'jackpot',
'jackson_arvad',
'jacob_jake_fury',
'jacqueline_falsworth',
'jacques_duquesne',
'jade_dragon',
'jaeger',
'jaguar',
'jamal_afari',
'james_jimmy_marks',
'james_dr_power',
'james_howlett',
'james_jaspers',
'james_madrox',
'james_proudstar',
'james_rhodes',
'james_sanders',
'jamie_braddock',
'jane_foster',
'jane_kincaid',
'janet_van_dyne',
'jann',
'janus',
'jared_corbo',
'jarella',
'jaren',
'jason',
'jawynn_dueck_the_iron_christian_of_faith',
'jazz',
'jean_dewolff',
'jean_grey',
'jean_grey_summers',
'jean_paul_beaubier',
'jeanne_marie_beaubier',
'jebediah_guthrie',
'jeffrey_mace',
'jekyll',
'jennifer_kale',
'jennifer_walters',
'jens_meilleur_slap_shot',
'jericho_drumm',
'jerome_beechman',
'jerry_jaxon',
'jessica_drew',
'jessica_jones',
'jester',
'jigsaw',
'jim_hammond',
'jimaine_szardos',
'jimmy_woo',
'jocasta',
'joe_cartelli',
'joe_fixit',
'joey_bailey',
'johann_schmidt',
'john_doe',
'john_falsworth',
'john_jameson',
'john_proudstar',
'john_ryker',
'john_sublime',
'john_walker',
'johnny_blaze',
'johnny_ohm',
'johnny_storm',
'jolt',
'jon_spectre',
'jonas_harrow',
'jonathan_john_garrett',
'jonathan_richards',
'jonothon_starsmore',
'jordan_seberius',
'joseph',
'joshua_guthrie',
'joystick',
'jubilee',
'judas_traveller',
'jude_the_entropic_man',
'juggernaut',
'julie_power',
'jumbo_carnation',
'junkpile',
'junta',
'justice',
'justin_hammer',
'justine_hammer',
'ka_zar',
'kaine',
'kala',
'kalu',
'kamal',
'kamo_tharnn',
'kamu',
'kang_the_conqueror',
'kangaroo',
'karen_page',
'karima_shapandar',
'karkas',
'karl_lykos',
'karl_malus',
'karl_mordo',
'karla_sofen',
'karma',
'karnak',
'karnilla',
'karolina_dean',
'karthon_the_quester',
'kasper_cole',
'kate_bishop',
'kate_neville',
'katherine_kitty_pryde',
'katherine_reynolds',
'katie_power',
'katrina_luisa_van_horne',
'kat',
'keen_marlow',
'kehl_of_tauran',
'keith_kilham',
'kem_horkus',
'kenneth_crichton',
'key',
'khaos',
'khonsh',
'khoryphos',
'kiber_the_cruel',
'kick_ass',
'kid_colt',
'kid_nova',
'kiden_nixon',
'kierrok',
'killer_shrike',
'killpower',
'killraven',
'kilmer',
'kimura',
'king_bedlam',
'kingo_sunen',
'kingpin',
'kirigi',
'kirtsyn_perrin_short_stop',
'kismet',
'kismet_deadly',
'kiss',
'kiwi_black',
'kkallakk',
'klrt',
'klaat',
'klaw',
'kleinstocks',
'knickknack',
'kofi_whitemane',
'kogar',
'kohl_harder_boulder_man',
'korath_the_pursuer',
'korg',
'kormok',
'korrek',
'korvac',
'korvus',
'kosmos',
'kraken',
'krakkan',
'krang',
'kraven_the_hunter',
'krista_marwan',
'kristoff_vernard',
'kristoff_von_doom',
'kro',
'krystalin',
'kubik',
'kukulcan',
'kurse',
'kurt_wagner',
'kwannon',
'kyle_gibney',
'kylun',
'kymaera',
'la_lunatica',
'la_nuit',
'lacuna',
'lady_deathstrike',
'lady_jacqueline_falsworth_crichton',
'lady_killer',
'lady_lark',
'lady_lotus',
'lady_mandarin',
'lady_mastermind',
'lady_octopus',
'lament',
'lancer',
'landslide',
'larry_bodine',
'lasher',
'laura_dean',
'layla_miller',
'lazarus',
'leader',
'leap_frog',
'leash',
'lee_forrester',
'leech',
'left_hand',
'left_winger',
'legacy',
'legion',
'leila_davis',
'leir',
'lemuel_dorcas',
'leo',
'leonard_samson',
'leonus',
'letha',
'levan',
'lianda',
'libra',
'lifeforce',
'lifeguard',
'lifter',
'lightbright',
'lighting_rod',
'lightmaster',
'lightspeed',
'lila_cheney',
'lilandra_neramani',
'lilith_the_daughter_of_dracula',
'lin_sun',
'link',
'lionheart',
'live_wire',
'living_brain',
'living_colossus',
'living_diamond',
'living_eraser',
'living_hulk',
'living_laser',
'living_lightning',
'living_monolith',
'living_mummy',
'living_pharaoh',
'living_planet',
'living_totem',
'living_tribunal',
'liz_allan',
'lizard',
'llan_the_sorcerer',
'lloigoroth',
'llyra',
'llyron',
'loa',
'lockdown',
'lockheed',
'lockjaw',
'locksmith',
'locus',
'locust',
'lodestone',
'logan',
'loki',
'longneck',
'longshot',
'lonnie_thompson_lincoln',
'looter',
'lord_chaos',
'lord_dark_wind',
'lord_pumpkin',
'lorelei',
'lorelei_ii',
'lorelei_travis',
'lorna_dane',
'lorvex',
'loss',
'louise_mason',
'lucas_brand',
'luchino_nefaria',
'lucifer',
'ludi',
'luke_cage',
'luna',
'lunatica',
'lunatik',
'lupa',
'lupo',
'lurking_unknown',
'lyja',
'lynx',
'm',
'm_twins',
'mn_e_ultraverse',
'modam',
'modok',
'mac_gargan',
'mach_iv',
'machine_man',
'machine_teen',
'machinesmith',
'mad_dog_rassitano',
'mad_jack',
'mad_jim_jaspers',
'mad_thinker',
'mad_thinkers_awesome_android',
'mad_dog',
'madam_slay',
'madame_hydra',
'madame_macevil',
'madame_masque',
'madame_menace',
'madame_web',
'madcap',
'madeline_joyce',
'madelyne_pryor',
'madison_jeffries',
'maelstrom',
'maestro',
'magdalena',
'magdalene',
'maggott',
'magician',
'magik',
'magilla',
'magma',
'magneto',
'magnum',
'magnus',
'magus',
'maha_yogi',
'mahkizmo',
'major_mapleleaf',
'makkari',
'malekith_the_accursed',
'malice',
'mammomax',
'man_mountain_marko',
'man_ape',
'man_beast',
'man_brute',
'man_bull',
'man_eater',
'man_elephant',
'man_killer',
'man_spider',
'man_thing',
'man_wolf',
'manbot',
'mandarin',
'mandrill',
'mandroid',
'mangle',
'mangog',
'manikin',
'manslaughter',
'manta',
'mantis',
'mantra',
'mar_vell',
'marc_spector',
'marduk_kurios',
'margali_szardos',
'margaret_power',
'margo_damian',
'maria_hill',
'mariko_yashida',
'marius_st_croix',
'mark_gervaisnight_shade',
'mark_raxton',
'mark_scarlotti',
'mark_todd',
'marlene_alraune',
'marrina',
'marrina_smallwood',
'marrow',
'marsha_rosenberg',
'martha_johansson',
'martin_gold',
'martin_preston',
'martinex',
'marvel_boy',
'marvel_girl',
'marvel_man',
'marvin_flumm',
'mary_skeeter_macpherran',
'mary_jane_parker',
'mary_jane_watson',
'mary_walker',
'mary_zero',
'masked_marauder',
'masked_marvel',
'masked_rose',
'masque',
'mass_master',
'master_khan',
'master_man',
'master_menace',
'master_mold',
'master_order',
'master_pandemonium',
'master_of_vengeance',
'mastermind',
'mastermind_of_the_uk',
'matador',
'match',
'matsuo_tsurayaba',
'matt_murdock',
'mauler',
'maur_konn',
'mauvais',
'maverick',
'max',
'maxam',
'maximus',
'maxwell_dillon',
'may_mayday_parker',
'may_parker',
'mayhem',
'maynard_tiboldt',
'meanstreak',
'meathook',
'mechamage',
'medusa',
'meggan',
'meggan_braddock',
'mekano',
'meld',
'melee',
'melissa_gold',
'melody_guthrie',
'meltdown',
'melter',
'mentallo',
'mentor',
'mentus',
'mephisto',
'mercurio',
'mercury',
'mercy',
'merlin',
'mesmero',
'metal_master',
'metalhead',
'meteor_man',
'meteorite',
'meteorite_ii',
'michael_nowman',
'michael_twoyoungmen',
'micro',
'microchip',
'micromax',
'midas',
'midgard_serpent',
'midnight',
'midnight_man',
'midnight_sun',
'miek',
'miguel_espinosa',
'miguel_ohara',
'miguel_santos',
'mikado',
'mikey',
'mikhail_rasputin',
'mikula_golubev',
'milan',
'miles_warren',
'milos_masaryk',
'mimic',
'mimir',
'mindmeld',
'mindworm',
'miracle_man',
'mirage',
'mirage_ii',
'misfit',
'miss_america',
'missing_link',
'mist_mistress',
'mister_buda',
'mister_doll',
'mister_fear',
'mister_hyde',
'mister_jip',
'mister_machine',
'mister_one',
'mister_sensitive',
'mister_sinister',
'mister_two',
'mister_x',
'misty_knight',
'mockingbird',
'modred_the_mystic',
'mogul_of_the_mystic_mountain',
'moira_brandon',
'moira_mactaggert',
'mojo',
'mole_man',
'molecule_man',
'molly_hayes',
'molten_man',
'mondo',
'monet_st_croix',
'mongoose',
'monica_rappaccini',
'monsoon',
'monstra',
'monstro_the_mighty',
'moon_knight',
'moon_boy',
'moondark',
'moondragon',
'moonhunter',
'moonstone',
'mop_man',
'morbius',
'mordred',
'morg',
'morgan_le_fay',
'morlun',
'morning_star',
'morph',
'morpheus',
'morris_bench',
'mortimer_toynbee',
'moses_magnum',
'mosha',
'mother_earth',
'mother_nature',
'mother_night',
'mother_superior',
'motormouth',
'mountjoy',
'mr_fish',
'mr_justice',
'mr_m',
'mr_w',
'ms_modok',
'ms_marvel',
'ms_steed',
'multiple_man',
'murmur',
'murmur_ii',
'mutant_master',
'mutant_x',
'myron_maclain',
'mys_tech',
'mysterio',
'mystique',
'ngabthoth',
'ngarai',
'nastirh',
'nfl_superpro',
'naga',
'nameless_one',
'namor_mckenzie',
'namor_the_sub_mariner',
'namora',
'namorita',
'nanny',
'nate_grey',
'nathaniel_essex',
'nathaniel_richards',
'native',
'nebula',
'nebulo',
'nebulon',
'nebulos',
'necrodamus',
'necromantra',
'ned_horrocks',
'ned_leeds',
'needle',
'nefarius',
'negasonic_teenage_warhead',
'nekra',
'nekra_sinclar',
'nemesis',
'neophyte',
'neptune',
'network',
'neuronne',
'neurotap',
'new_goblin',
'nezarr_the_calculator',
'nicholas_maunder',
'nicholas_scratch',
'nick_fury',
'nico_minor',
'nicole_st_croix',
'night_nurse',
'night_rider',
'night_thrasher',
'nightcrawler',
'nighthawk',
'nightmare',
'nightshade',
'nightside',
'nightwatch',
'nightwind',
'nikki',
'niles_van_roekel',
'nimrod',
'ningal',
'nitro',
'nobilus',
'nocturne',
'noh_varr',
'nomad',
'norman_osborn',
'norns',
'norrin_radd',
'northstar',
'nosferata',
'nova',
'nova_prime',
'novs',
'nox',
'nth_man',
'nth_man_the_ultimate_ninja',
'nuke_frank_simpson',
'nuke_squadron_supreme_member',
'nuklo',
'numinus',
'nut',
'obadiah_stane',
'obituary',
'obliterator',
'oblivion',
'occulus',
'ocean',
'ocelot',
'oddball',
'odin',
'ogre',
'ogress',
'omega',
'omega_red',
'omega_the_unknown',
'omen',
'omerta',
'one_above_all',
'oneg_the_prober',
'onslaught',
'onyxx',
'ooze',
'optoman',
'oracle',
'orator',
'orb',
'orbit',
'orchid',
'ord',
'order',
'orikal',
'orka',
'ororo_munroe',
'orphan',
'orphan_maker',
'osiris',
'outlaw',
'outrage',
'overkill',
'overmind',
'overrider',
'owl',
'ox',
'ozone',
'ozymandias',
'paibo',
'paige_guthrie',
'paladin',
'paradigm',
'paragon',
'paralyzer',
'paris',
'pasco',
'paste_pot_pete',
'patch',
'pathway',
'patriot',
'patriot_ii',
'patsy_hellstrom',
'patsy_walker',
'paul_bailey',
'paul_norbert_ebersol',
'paul_patterson',
'payback',
'peace_monger',
'peepers',
'peggy_carter',
'penance',
'penance_ii',
'peregrine',
'perfection',
'perseus',
'persuader',
'persuasion',
'perun',
'pete_wisdom',
'peter_criss',
'peter_noble',
'peter_parker',
'peter_petruski',
'phade',
'phage',
'phalanx',
'phantazia',
'phantom_blonde',
'phantom_eagle',
'phantom_rider',
'phastos',
'phat',
'phil_urich',
'philip_fetter',
'phineas_t_horton',
'phoenix',
'photon',
'phyla_vell',
'pietro_maximoff',
'piledriver',
'piotr_rasputin',
'pip_the_troll',
'pipeline',
'piper',
'piranha',
'pisces',
'pistol',
'pixie',
'pixx',
'plague',
'plantman',
'plasma',
'plazm',
'plug',
'plunderer',
'pluto',
'poison',
'polaris',
'poltergeist',
'porcupine',
'portal',
'possessor',
'postman',
'postmortem',
'poundcakes',
'powderkeg',
'power_broker',
'power_man',
'power_princess',
'power_skrull',
'powerhouse',
'powerpax',
'presence',
'pressure',
'prester_john',
'pretty_persuasions',
'preview',
'primal',
'prime',
'prime_mover',
'primevil',
'primus',
'princess_python',
'proctor',
'prodigy',
'professor_power',
'professor_x',
'projector',
'prometheus',
'protector',
'proteus',
'prototype',
'prowler',
'psi_lord',
'psyche',
'psycho_man',
'psyklop',
'psylocke',
'puck',
'puff_adder',
'puishannt',
'pulse',
'puma',
'punchout',
'punisher',
'punisher_2099',
'puppet_master',
'purge',
'purple_girl',
'purple_man',
'pyre',
'pyro',
'quagmire',
'quantum',
'quasar',
'quasar_ii',
'quasimodo',
'quentin_beck',
'quentin_quire',
'quicksand',
'quicksilver',
'quincy_harker',
'raa_of_the_caves',
'rachel_grey',
'rachel_summers',
'rachel_van_helsing',
'radian',
'radioactive_man',
'radion_the_atomic_man',
'radius',
'rafferty',
'rage',
'raggadorr',
'rahne_sinclair',
'rainbow',
'rama_tut',
'raman',
'ramrod',
'ramshot',
'rancor',
'randall_shire',
'random',
'ranger',
'ransak_the_reject',
'rattler',
'ravage_2099',
'raving_beauty',
'rawhide_kid',
'rax',
'raymond_sikorsky',
'raza',
'razor_fist',
'razorback',
'reaper',
'rebel',
'recorder',
'red_claw',
'red_ghost',
'red_guardian',
'red_lotus',
'red_nine',
'red_raven',
'red_ronin',
'red_shift',
'red_skull',
'red_skull_ii',
'red_wolf',
'redeemer',
'redneck',
'redwing',
'reeva_payge',
'reignfire',
'reject',
'remnant',
'remy_lebea',
'reptyl',
'revanche',
'rex_mundi',
'rhiannon',
'rhino',
'ricadonna',
'richard_fisk',
'richard_parker',
'richard_rider',
'rick_jones',
'ricochet',
'rictor',
'rigellian_recorder',
'right_winger',
'ringer',
'ringleader',
'ringmaster',
'ringo_kid',
'rintrah',
'riot',
'riot_grrl',
'ripfire',
'ritchie_gilmore',
'rlnnd',
'robbie_robertson',
'robert_bobby_drake',
'robert_bruce_banner',
'robert_hunter',
'robert_kelly',
'robert_da_costa',
'rock',
'rock_python',
'rocket_raccoon',
'rocket_racer',
'rodstvow',
'rogue',
'rom_the_spaceknight',
'roma',
'romany_wisdom',
'ronan_the_accuser',
'rose',
'roughhouse',
'roulette',
'royal_roy',
'ruby_thursday',
'ruckus',
'rumiko_fujikawa',
'rune',
'runner',
'rush',
'rusty_collins',
'ruth_bat_seraph',
'ryder',
'sbyll',
'sym',
'sabra',
'sabreclaw',
'sabretooth',
'sack',
'sage',
'sagittarius',
'saint_anna',
'saint_elmo',
'sally_blevins',
'sally_floyd',
'salvo',
'sam_sawyer',
'sam_wilson',
'samuel_starr_saxon',
'samuel_guthrie',
'samuel_silke',
'samuel_smithers',
'sandman',
'sangre',
'sara_grey',
'sasquatch',
'satana',
'satannish',
'saturnyne',
'sauron',
'savage_steel',
'sayge',
'scaleface',
'scalphunter',
'scanner',
'scarecrow',
'scarecrow_ii',
'scarlet_beetle',
'scarlet_centurion',
'scarlet_scarab',
'scarlet_spider',
'scarlet_spiders',
'scarlet_witch',
'schemer',
'scimitar',
'scintilla',
'scorcher',
'scorpia',
'scorpio',
'scorpion',
'scott_summers',
'scott_washington',
'scourge_of_the_underworld',
'scrambler',
'scream',
'screaming_mimi',
'screech',
'scrier',
'sea_urchin',
'seamus_mellencamp',
'sean_cassidy',
'sean_garrison',
'sebastian_shaw',
'seeker',
'sekhmet',
'selene',
'senator_robert_kelly',
'senor_muerte',
'sentry',
'sepulchre',
'sergeant_fury',
'sergei_kravinoff',
'serpentina',
'sersi',
'set',
'seth',
'shadow_king',
'shadow_slasher',
'shadow_hunter',
'shadowcat',
'shadowmage',
'shadrac',
'shalla_bal',
'shaman',
'shamrock',
'shang_chi',
'shanga',
'shanna_the_she_devil',
'shaper_of_worlds',
'shard',
'sharon_carter',
'sharon_friedlander',
'sharon_ventura',
'shathra',
'shatter',
'shatterfist',
'shatterstar',
'she_hulk',
'she_thing',
'she_venom',
'shellshock',
'shen_kuei',
'shiar_gladiator',
'shinchuko_lotus',
'shingen_harada',
'shinobi_shaw',
'shirow_ishihara',
'shiva',
'shiver_man',
'shocker',
'shockwave',
'shola_inkosi',
'shooting_star',
'shotgun',
'shriek',
'shriker',
'shroud',
'shrunken_bones',
'shuma_gorath',
'sidewinder',
'siege',
'siena_blaze',
'sif',
'sigmar',
'sigyn',
'sikorsky',
'silhouette',
'silly_seal',
'silver',
'silver_dagger',
'silver_fox',
'silver_sable',
'silver_samurai',
'silver_scorpion',
'silver_squire',
'silver_surfer',
'silverclaw',
'silvermane',
'simon_williams',
'sin',
'sin_eater',
'sinister',
'sir_steel',
'siryn',
'sise_neg',
'skein',
'skids',
'skin',
'skinhead',
'skull_the_slayer',
'skullcrusher',
'skullfire',
'skunge_the_laxidazian_troll',
'skyhawk',
'skywalker',
'slab',
'slapstick',
'sleek',
'sleeper',
'sleepwalker',
'slick',
'sligguth',
'slipstream',
'slither',
'sludge',
'slug',
'sluggo',
'sluk',
'slyde',
'smart_alec',
'smartship_friday',
'smasher',
'smuggler',
'smuggler_ii',
'snowbird',
'snowfall',
'solara',
'solarman',
'solarr',
'soldier_x',
'solitaire',
'solo',
'solomon_osullivan',
'son_of_satan',
'songbird',
'soulfire',
'space_phantom',
'space_turnip',
'specialist',
'spectra',
'spectral',
'speed',
'speed_demon',
'speedball',
'speedo',
'spellbinder',
'spellcheck',
'spencer_smythe',
'sphinx',
'sphinxor',
'spider_doppelganger',
'spider_girl',
'spider_ham',
'spider_man',
'spider_slayer',
'spider_woman',
'spidercide',
'spike',
'spike_freeman',
'spinnerette',
'spiral',
'spirit_of_76',
'spitfire',
'spoilsport',
'spoor',
'spot',
'sprite',
'sputnik',
'spyder',
'spymaster',
'spyne',
'squidboy',
'squirrel_girl',
'st_john_allerdyce',
'stacy_x',
'stained_glass_scarlet',
'stakar',
'stallior',
'stanley_stewart',
'star_stalker',
'star_thief',
'star_dancer',
'star_lord',
'starbolt',
'stardust',
'starfox',
'starhawk',
'starlight',
'starr_the_slayer',
'starshine',
'starstreak',
'stature',
'steel_raven',
'steel_serpent',
'steel_spider',
'stegron',
'stellaris',
'stem_cell',
'stentor',
'stephen_colbert',
'stephen_strange',
'steve_rogers',
'steven_lang',
'stevie_hunter',
'stick',
'stiletto',
'stilt_man',
'stinger',
'stingray',
'stitch',
'stone',
'stonecutter',
'stonewall',
'storm',
'stranger',
'stratosfire',
'straw_man',
'strobe',
'strong_guy',
'strongarm',
'stryfe',
'stunner',
'stuntmaster',
'stygorr',
'stygyro',
'styx_and_stone',
'sub_mariner',
'sugar_man',
'suicide',
'sultan',
'sun_girl',
'sunder',
'sundragon',
'sunfire',
'sunpyre',
'sunset_bain',
'sunspot',
'sunstreak',
'sunstroke',
'sunturion',
'super_rabbit',
'super_sabre',
'super_adaptoid',
'super_nova',
'super_skrull',
'superpro',
'supercharger',
'superia',
'supernalia',
'suprema',
'supreme_intelligence',
'supremor',
'surge',
'surtur',
'susan_richards',
'susan_storm',
'sushi',
'svarog',
'swarm',
'sweetface',
'swordsman',
'sybil_dorn',
'sybil_dvorak',
'synch',
't_ray',
'tabitha_smith',
'tag',
'tagak_the_leopard_lord',
'tailhook',
'taj_nital',
'talia_josephine_wagner',
'talisman',
'tamara_rahn',
'tana_nile',
'tantra',
'tanya_anderssen',
'tarantula',
'tarot',
'tartarus',
'taskmaster',
'tatterdemalion',
'tattletale',
'tattoo',
'taurus',
'techno',
'tefral_the_surveyor',
'tempest',
'tempo',
'tempus',
'temugin',
'tenpin',
'termagaira',
'terminator',
'terminatrix',
'terminus',
'terrax_the_tamer',
'terraxia',
'terror',
'tess_one',
'tessa',
'tether',
'tethlam',
'tex_dawson',
'texas_twister',
'thakos',
'thane_ector',
'thanos',
'the_amazing_tanwir_ahmed',
'the_angel',
'the_blank',
'the_destroyer',
'the_entity',
'the_grip',
'the_night_man',
'the_profile',
'the_russian',
'the_stepford_cuckoos',
'the_symbiote',
'the_wink',
'thena',
'theresa_cassidy',
'thermo',
'thin_man',
'thing',
'thinker',
'thirty_three',
'thog',
'thomas_halloway',
'thor',
'thor_girl',
'thornn',
'threnody',
'thumbelina',
'thunderball',
'thunderbird',
'thunderbolt',
'thunderclap',
'thunderfist',
'thunderstrike',
'thundra',
'tiboro',
'tiger_shark',
'tigra',
'timberius',
'time_bomb',
'timeshadow',
'timeslip',
'tinkerer',
'titan',
'titania',
'titanium_man',
'tito_bohusk',
'toad',
'toad_in_waiting',
'todd_arliss',
'tom_cassidy',
'tom_corsi',
'tom_foster',
'tom_thumb',
'tomazooma',
'tombstone',
'tommy',
'tommy_lightning',
'tomorrow_man',
'tony_stark',
'topaz',
'topspin',
'torgo_of_mekka',
'torgo_the_vampire',
'toro',
'torpedo',
'torrent',
'torso',
'tower',
'toxin',
'trader',
'trapper',
'trapster',
'tremolo',
'trevor_fitzroy',
'tri_man',
'triathlon',
'trick_shot',
'trioccula',
'trip_monroe',
'triton',
'troll',
'trump',
'tuc',
'tugun',
'tumbler',
'tundra',
'turac',
'turbo',
'turner_century',
'turner_d_century',
'tusk',
'tutinax_the_mountain_mover',
'two_gun_kid',
'tyger_tiger',
'typeface',
'typhoid',
'typhoid_mary',
'typhon',
'tyr',
'tyrak',
'tyrannosaur',
'tyrannus',
'tyrant',
'tzabaoth',
'u_go_girl',
'u_man',
'usagent',
'uat',
'ulik',
'ultimo',
'ultimus',
'ultra_marine',
'ultragirl',
'ultron',
'ulysses',
'umar',
'umbo',
'uncle_ben_parker',
'uni_mind',
'unicorn',
'union_jack',
'unseen',
'unthinnk',
'unus_the_untouchable',
'unuscione',
'ursa_major',
'urthona',
'utgard_loki',
'vagabond',
'vague',
'vakume',
'valentina_allegra_de_la_fontaine',
'valerie_cooper',
'valinor',
'valkin',
'valkyrie',
'valtorr',
'vamp',
'vampire_by_night',
'vance_astro',
'vance_astrovik',
'vanguard',
'vanisher',
'vapor',
'vargas',
'varnae',
'vashti',
'vavavoom',
'vector',
'vegas',
'veil',
'vengeance',
'venom',
'venomm',
'venus',
'venus_dee_milo',
'veritas',
'vermin',
'vertigo',
'vesta',
'vibraxas',
'vibro',
'victor_creed',
'victor_mancha',
'victor_strange',
'victor_von_doom',
'victorius',
'vidar',
'vincente',
'vindaloo',
'vindicator',
'viper',
'virako',
'virginia_pepper_potts',
'virgo',
'vishanti',
'visimajoris',
'vision',
'vivisector',
'vixen',
'volcana',
'volla',
'volpan',
'volstagg',
'vulcan',
'vulture',
'wade_wilson',
'wallflower',
'walter_newell',
'wanda_maximoff',
'war',
'war_eagle',
'war_machine',
'war_v',
'warbird',
'warhawk',
'warlock',
'warpath',
'warren_iii_worthington',
'warrior_woman',
'warstar',
'warstrike',
'warwolves',
'washout',
'wasp',
'watcher',
'water_wizard',
'watoomb',
'weapon_x',
'wendell_vaughn',
'wendigo',
'werewolf_by_night',
'western_kid',
'whiplash',
'whirlwind',
'whistler',
'white_fang',
'white_pilgrim',
'white_queen',
'white_rabbit',
'white_tiger',
'whiteout',
'whizzer',
'wiccan',
'wicked',
'widget',
'wilbur_day',
'wild_child',
'wild_thing',
'wildboys',
'wildpride',
'wildside',
'will_o_the_wisp',
'william_baker',
'william_stryker',
'willie_lumpkin',
'wilson_fisk',
'wind_dancer',
'wind_warrior',
'windeagle',
'windshear',
'winky_man',
'winter_soldier',
'witchfire',
'wiz_kid',
'wizard',
'wolf',
'wolfsbane',
'wolverine',
'wonder_man',
'wong',
'woodgod',
'worm',
'wraith',
'wrath',
'wreckage',
'wrecker',
'wundarr_the_aquarian',
'wyatt_wingfoot',
'wysper',
'x_23',
'x_cutioner',
'x_man',
'x_ray',
'x_treme',
'xand',
'xavin',
'xemnu_the_titan',
'xem',
'xian_chi_xan',
'xorn',
'xorr_the_god_jewel',
'ygaron',
'yandroth',
'yellow_claw',
'yellowjacket',
'yeti',
'yith',
'ymir',
'yond',
'yrial',
'yukio',
'yukon_jack',
'yuri_topolov',
'yuriko_oyama',
'zab',
'zach',
'zaladane',
'zarathos',
'zarek',
'zartra',
'zebediah_killgrave',
'zeitgeist',
'zero',
'zero_g',
'zeus',
'ziggy_pig',
'zip_zap',
'zodiak',
'zom',
'zombie',
'zuras',
'zzzax',
'gen_harada',
'the_living_colossus_it',
'the_living_darkness_null',
'the_renegade_watcher_aron',
'the_tomorrow_man_zarrko'
]


def get_float_from_string(seed):
    ''' Probably bad way to get a float from secret key'''
    max_sha_float = float(115792089237316195423570985008687907853269984665640564039457584007913129639935)
    h = hashlib.sha256(seed.encode('utf-8'))
    return int(h.hexdigest(), 16) / max_sha_float


def shuffle_list(original, seed):
    ''' Same shuffle for same seed'''
    float_seed = get_float_from_string(seed)
    return random.shuffle(original, lambda: float_seed)


shuffle_list(NAMES, settings.SECRET_KEY)


def get_name_from_number(num):
    x = num % len(NAMES)
    return NAMES[x]
