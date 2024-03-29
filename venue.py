from enum import Enum

# Supported publication types
class PubType(Enum):
    PROCEEDING = 'Conference and Workshop Papers'
    JOURNAL = 'Journal Articles'
    ARXIV = 'Informal and Other Publications'
    

# dblp_id: each conf/journal is allocated with an id by dblp database
# This is predefined booktitles/journals for abbreviation in dblp_id
# conferences/journals from ccf 2022 list
venue_dict = {
        PubType.PROCEEDING: {
            "ppopp": "{ACM} PPoPP",
            "fast": "{USENIX} {FAST}",
            "dac": "{ACM} {DAC}",
            "hpca": "{IEEE} {HPCA}",
            "micro": "{IEEE/ACM} {MICRO}",
            "sc": "{IEEE} {SC}",
            "asplos": "{ACM} {ASPLOS}",
            "isca": "{ACM/IEEE} {ISCA}",
            "usenix": "{USENIX} {ATC}",
            "eurosys": "{ACM} EuroSys",
            "cloud": "{ACM} SoCC",
            "spaa": "{ACM} {SPAA}",
            "podc": "{ACM} {PODC}",
            "fpga": "{ACM} {FPGA}",
            "cgo": "{IEEE/ACM} {CGO}",
            "date": "{IEEE/ACM} {DATE}",
            "hotchips": "{IEEE} {HOT} {CHIPS}",
            "cluster": "{IEEE} {CLUSTER}",
            "iccd": "{IEEE} {ICCD}",
            "iccad": "{IEEE/ACM} {ICCAD}",
            "icdcs": "{IEEE} {ICDCS}",
            "codesisss": "{ACM/IEEE} CODES ISSS",
            "hipeac": "{ACM} HiPEAC",
            "sigmetrics": "{ACM} {SIGMETRICS}",
            "IEEEpact": "{IEEE/ACM} {PACT}",
            "icpp": "{ACM} {ICPP}",
            "ics": "{ACM} {ICS}",
            "vee": "{ACM} {VEE}",
            "ipps": "{IEEE} {IPDPS}",
            "performance": "{ACM} Performance",
            "hpdc": "{IEEE} {HPDC}",
            "itc": "{IEEE} {ITC}",
            "lisa": "{USENIX} {LISA}",
            "mss": "{IEEE} {MSST}",
            "rtas": "{IEEE} {RTAS}",
            "europar": "Springer Euro-Par",
            "cf": "{ACM} {CF}",
            "systor": "{ACM} {SYSTOR}",
            "nocs": "{ACM/IEEE} {NOCS}",
            "asap": "{IEEE} {ASAP}",
            "aspdac": "{ACM/IEEE} {ASP-DAC}",
            "ets": "{IEEE} {ETS}",
            "fpl": "{IEEE} {FPL}",
            "fccm": "{IEEE} {FCCM}",
            "glvlsi": "{ACM/IEEE} {GLSVLSI}",
            "ats": "{IEEE} {ATS}",
            "hpcc": "{IEEE} {HPCC}",
            "hipc": "{IEEE/ACM} HiPC",
            "mascots": "{IEEE} {MASCOTS}",
            "ispa": "{IEEE} {ISPA}",
            "ccgrid": "{ACM/IEEE} {CCGRID}",
            "npc": "Springer {NPC}",
            "ica3pp": "{IEEE} ICA3PP",
            "cases": "{ACM} {CASES}",
            "fpt": "{IEEE} {FPT}",
            "icpads": "{IEEE} {ICPADS}",
            "iscas": "{IEEE} {ISCAS}",
            "islped": "{ACM/IEEE} {ISLPED}",
            "ispd": "{ACM} {ISPD}",
            "hoti": "{IEEE} {HOTI}",
            "vts": "{IEEE} {VTS}",
            "sigcomm": "{ACM} {SIGCOMM}",
            "mobicom": "{ACM} MobiCom",
            "infocom": "{IEEE} {INFOCOM}",
            "nsdi": "{USENIX} {NSDI}",
            "sensys": "{ACM} SenSys",
            "conext": "{ACM} CoNEXT",
            "secon": "{IEEE} {SECON}",
            "ipsn": "{IEEE/ACM} {IPSN}",
            "mobisys": "{ACM} MobiSys",
            "icnp": "{IEEE} {ICNP}",
            "mobihoc": "{ACM/IEEE} MobiHoc",
            "nossdav": "{ACM} {NOSSDAV}",
            "iwqos": "{IEEE} IWQoS",
            "imc": "{ACM/USENIX} {IMC}",
            "ancs": "{ACM/IEEE} {ANCS}",
            "apnoms": "{IFIP/IEEE} {APNOMS}",
            "forte": "Springer {FORTE}",
            "lcn": "{IEEE} {LCN}",
            "globecom": "{IEEE} {GLOBECOM}",
            "icc": "{IEEE} {ICC}",
            "icccn": "{IEEE} {ICCCN}",
            "mass": "{IEEE} {MASS}",
            "p2p": "{IEEE} P2P",
            "ipccc": "{IEEE} {IPCCC}",
            "wowmom": "{IEEE} WoWMoM",
            "iscc": "{IEEE} {ISCC}",
            "wcnc": "{IEEE} {WCNC}",
            "networking": "{IFIP} Networking",
            "im": "{IFIP/IEEE} {IM}",
            "msn": "{IEEE} {MSN}",
            "mswim": "{ACM} MSWiM",
            "wasa": "Springer {WASA}",
            "hotnets": "{ACM} HotNets",
            "apnet": "{ACM} APNet",
            "ccs": "{ACM} {CCS}",
            "eurocrypt": "Springer {EUROCRYPT}",
            "sp": "{IEEE} S\\&P",
            "crypto": "Springer {CRYPTO}",
            "uss": "{USENIX} Security",
            "ndss": "{ISOC} {NDSS}",
            "acsac": "{IEEE} {ACSAC}",
            "asiacrypt": "Springer {ASIACRYPT}",
            "esorics": "Springer {ESORICS}",
            "fse": "Springer {FSE}",
            "csfw": "{IEEE} {CSFW}",
            "srds": "{IEEE} {SRDS}",
            "ches": "Springer {CHES}",
            "dsn": "{IEEE/IFIP} {DSN}",
            "raid": "Springer {RAID}",
            "pkc": "Springer {PKC}",
            "tcc": "Springer {TCC}",
            "wisec": "{ACM} WiSec",
            "sacmat": "{ACM} {SACMAT}",
            "drm": "{ACM} {DRM}",
            "ih": "{ACM} IH\\&MMSec",
            "acns": "Springer {ACNS}",
            "asiaccs": "{ACM} AsiaCCS",
            "acisp": "Springer {ACISP}",
            "ctrsa": "Springer {CT-RSA}",
            "dimva": "{DIMVA}",
            "dfrws": "Elsevier {DFRWS}",
            "fc": "Springer {FC}",
            "trustcom": "{IEEE} TrustCom",
            "sec": "Springer {SEC}",
            "isw": "Springer {ISC}",
            "icdf2c": "Springer ICDF2C",
            "icics": "Springer {ICICS}",
            "securecomm": "{ACM} SecureComm",
            "nspw": "{ACM} {NSPW}",
            "pam": "Springer {PAM}",
            "pet": "Springer {PETS}",
            "sacrypt": "Springer {SAC}",
            "soups": "{USENIX} {SOUPS}",
            "eurosp": "{IEEE} EuroS\\&P",
            "cisc": "Springer Inscrypt",
            "pldi": "{ACM} {PLDI}",
            "popl": "{ACM} {POPL}",
            "sigsoft": "{ACM} {FSE/ESEC}",
            "sosp": "{ACM} {SOSP}",
            "oopsla": "{ACM} {OOPSLA}",
            "kbse": "{IEEE/ACM} {ASE}",
            "icse": "{ACM/IEEE} {ICSE}",
            "issta": "{ACM} {ISSTA}",
            "osdi": "{USENIX} {OSDI}",
            "fm": "{FME} {FM}",
            "ecoop": "{AITO} {ECOOP}",
            "etaps": "Springer {ETAPS}",
            "iwpc": "{IEEE} {ICPC}",
            "re": "{IEEE} {RE}",
            "caise": "Springer CAiSE",
            "icfp": "{ACM} {ICFP}",
            "lctrts": "{ACM} {LCTES}",
            "models": "{ACM/IEEE} , MoDELS",
            "cp": "Springer {CP}",
            "icsoc": "Springer {ICSOC}",
            "wcre": "{IEEE} {SANER}",
            "icsm": "{IEEE} {ICSME}",
            "vmcai": "Springer {VMCAI}",
            "icws": "{IEEE} {ICWS}",
            "middleware": "{ACM/IFIP/USENIX} Middleware",
            "sas": "Springer {SAS}",
            "esem": "{ACM/IEEE} {ESEM}",
            "issre": "{IEEE} {ISSRE}",
            "hotos": "{USENIX} HotOS",
            "pepm": "{ACM} {PEPM}",
            "paste": "{ACM} {PASTE}",
            "aplas": "Springer {APLAS}",
            "apsec": "{IEEE} {APSEC}",
            "ease": "{ACM} {EASE}",
            "iceccs": "{IEEE} {ICECCS}",
            "icst": "{IEEE} {ICST}",
            "ispass": "{IEEE} {ISPASS}",
            "scam": "{IEEE} {SCAM}",
            "compsac": "{IEEE} {COMPSAC}",
            "icfem": "Springer {ICFEM}",
            "tools": "Springer {TOOLS}",
            "IEEEscc": "{IEEE} {SCC}",
            "ispw": "{ACM} {ICSSP}",
            "seke": "{KSI} {SEKE}",
            "qrs": "{IEEE} {QRS}",
            "icsr": "Springer {ICSR}",
            "icwe": "Springer {ICWE}",
            "spin": "Springer {SPIN}",
            "atva": "Springer {ATVA}",
            "lopstr": "Springer {LOPSTR}",
            "tase": "{IEEE} {TASE}",
            "msr": "{IEEE/ACM} {MSR}",
            "refsq": "Springer {REFSQ}",
            "wicsa": "{IEEE} {WICSA}",
            "internetware": "{ACM} Internetware",
            "rv": "Springer {RV}",
            "sigmod": "{ACM} {SIGMOD}",
            "kdd": "{ACM} {SIGKDD}",
            "icde": "{IEEE} {ICDE}",
            "sigir": "{ACM} {SIGIR}",
            "vldb": "Morgan Kaufmann/ACM {VLDB}",
            "cikm": "{ACM} {CIKM}",
            "wsdm": "{ACM} {WSDM}",
            "pods": "{ACM} {PODS}",
            "dasfaa": "Springer {DASFAA}",
            "semweb": "{IEEE} {ISWC}",
            "icdm": "{IEEE} {ICDM}",
            "icdt": "Springer {ICDT}",
            "edbt": "Springer {EDBT}",
            "cidr": "Online Proceeding {CIDR}",
            "sdm": "{SIAM} {SDM}",
            "recsys": "{ACM} RecSys",
            "apweb": "Springer APWeb",
            "dexa": "Springer {DEXA}",
            "ecir": "Springer {ECIR}",
            "esws": "Springer {ESWC}",
            "webdb": "{ACM} WebDB",
            "er": "Springer {ER}",
            "mdm": "{IEEE} {MDM}",
            "ssdbm": "{IEEE} {SSDBM}",
            "waim": "Springer {WAIM}",
            "ssd": "Springer {SSTD}",
            "pakdd": "Springer {PAKDD}",
            "wise": "Springer {WISE}",
            "adma": "Springer {ADMA}",
            "stoc": "{ACM} {STOC}",
            "soda": "{SIAM} {SODA}",
            "cav": "Springer {CAV}",
            "focs": "{IEEE} {FOCS}",
            "lics": "{IEEE} {LICS}",
            "compgeom": "{ACM} SoCG",
            "esa": "Springer {ESA}",
            "coco": "{IEEE} {CCC}",
            "icalp": "Springer {ICALP}",
            "cade": "Springer ",
            "concur": "Springer {CONCUR}",
            "hybrid": "Springer and {ACM} {HSCC}",
            "sat": "Springer {SAT}",
            "cocoon": "Springer {COCOON}",
            "csl": "Springer {CSL}",
            "fmcad": "{ACM} {FMCAD}",
            "fsttcs": "Indian Association for Research in Computing Science {FSTTCS}",
            "dsaa": "{IEEE} {DSAA}",
            "ictac": "Springer {ICTAC}",
            "ipco": "Springer {IPCO}",
            "rta": "Springer {RTA}",
            "isaac": "Springer {ISAAC}",
            "mfcs": "Springer {MFCS}",
            "stacs": "Springer {STACS}",
            "setta": "Springer {SETTA}",
            "mm": "{ACM} {MM}",
            "siggraph": "{ACM} {SIGGRAPH}",
            "vr": "{IEEE} {VR}",
            "visualization": "{IEEE} {VIS}",
            "mir": "{ACM} {ICMR}",
            "si3d": "{ACM} I3D",
            "sca": "{ACM} {SCA}",
            "dcc": "{IEEE} {DCC}",
            "eurographics": "Wiley/Blackwell Eurographics",
            "vissym": "{ACM} EuroVis",
            "sgp": "Wiley/Blackwell {SGP}",
            "rt": "Wiley/Blackwell {EGSR}",
            "icassp": "{IEEE} {ICASSP}",
            "icmcs": "{IEEE} {ICME}",
            "ismar": "{IEEE/ACM} {ISMAR}",
            "pg": "Wiley/Blackwell {PG}",
            "sma": "SMA/Elsevier {SPM}",
            "vrst": "{ACM} {VRST}",
            "ca": "Wiley {CASA}",
            "cgi": "Springer {CGI}",
            "interspeech": "{ISCA} {INTERSPEECH}",
            "gmp": "Elsevier {GMP}",
            "apvis": "{IEEE} PacificVis",
            "3dim": "{IEEE} 3DV",
            "cadgraphics": "{IEEE} CAD/Graphics",
            "icip": "{IEEE} {ICIP}",
            "mmm": "Springer {MMM}",
            "mmasia": "{ACM} MMAsia",
            "smi": "{IEEE} {SMI}",
            "cvm": "Tsinghua University {CVM}",
            "prcv": "Springer {PRCV}",
            "aaai": "{AAAI} {AAAI}",
            "nips": "{MIT} Press NeurIPS",
            'iclr': "{ICLR}",
            "acl": "{ACL} {ACL}",
            "cvpr": "{IEEE} {CVPR}",
            "iccv": "{IEEE} {ICCV}",
            "icml": "{ACM} {ICML}",
            "ijcai": "Morgan Kaufmann {IJCAI}",
            "colt": "Springer {COLT}",
            "emnlp": "{ACL} {EMNLP}",
            "ecai": "{IOS} Press {ECAI}",
            "eccv": "Springer {ECCV}",
            "icra": "{IEEE} {ICRA}",
            "aips": "{AAAI} {ICAPS}",
            "iccbr": "Springer {ICCBR}",
            "coling": "International Committee on Computational Linguistics {COLING}",
            "kr": "Morgan Kaufmann {KR}",
            "uai": "{AUAI} {UAI}",
            "atal": "Springer {AAMAS}",
            "ppsn": "Springer {PPSN}",
            "naacl": "Association for Computational Linguistics {NAACL}",
            "aistats": "{JMLR} {AISTATS}",
            "accv": "Springer {ACCV}",
            "acml": "{JMLR} {ACML}",
            "bmvc": "British Machine Vision Association {BMVC}",
            "nlpcc": "Springer {NLPCC}",
            "conll": "Association for Computational Linguistics CoNLL",
            "gecco": "{ACM} {GECCO}",
            "ictai": "{IEEE} {ICTAI}",
            "iros": "{IEEE} {IROS}",
            "alt": "Springer {ALT}",
            "icann": "Springer {ICANN}",
            "fgr": "{IEEE} {FG}",
            "icdar": "{IEEE} {ICDAR}",
            "ilp": "Springer {ILP}",
            "ksem": "Springer {KSEM}",
            "iconip": "Springer {ICONIP}",
            "icpr": "{IEEE} {ICPR}",
            "icb": "{IEEE} {IJCB}",
            "ijcnn": "{IEEE} {IJCNN}",
            "pricai": "Springer {PRICAI}",
            "cscw": "{ACM} {CSCW}",
            "chi": "{ACM} {CHI}",
            "huc": "{ACM} UbiComp",
            "uist": "{ACM} {UIST}",
            "group": "{ACM} {GROUP}",
            "iui": "{ACM} {IUI}",
            "tabletop": "{ACM} {ITS}",
            "ecscw": "Springer {ECSCW}",
            "percom": "{IEEE} {PERCOM}",
            "mhci": "{ACM} MobileHCI",
            "icwsm": "{AAAI} {ICWSM}",
            "ACMdis": "{ACM} {DIS}",
            "icmi": "{ACM} {ICMI}",
            "assets": "{ACM} {ASSETS}",
            "graphicsinterface": "{ACM} {GI}",
            "uic": "{IEEE} {UIC}",
            "haptics": "{IEEE} ",
            "interact": "{IFIP} {INTERACT}",
            "acmidc": "{ACM} {IDC}",
            "colcom": "Springer CollaborateCom",
            "cscwd": "Springer {CSCWD}",
            "coopis": "Springer CoopIS",
            "mobiquitous": "Springer MobiQuitous",
            "avi": "{ACM} {AVI}",
            "www": "{ACM} {WWW}",
            "rtss": "{IEEE} {RTSS}",
            "wine": "Springer {WINE}",
            "cogsci": "Psychology Press CogSci",
            "bibm": "{IEEE} {BIBM}",
            "emsoft": "{ACM/IEEE/IFIP} {EMSOFT}",
            "ismb": "Oxford Journals {ISMB}",
            "recomb": "Springer {RECOMB}",
            "miccai": "Springer {MICCAI}",
            "amia": "{AMIA} {AMIA}",
            "apbc": "BioMed Central {APBC}",
            "bigdataconf": "{IEEE} BigData",
            "IEEEcloud": "{IEEE} {CLOUD}",
            "smc": "{IEEE} {SMC}",
            "cosit": "{ACM} {COSIT}",
            "isbra": "Springer {ISBRA}",
            "sagt": "Springer {SAGT}",
            "icic": "Springer-Nature {ICIC}",
            },
        PubType.JOURNAL: {
            "tocs": "{ACM} Trans. Comput. Syst.",
            "tos": "{ACM} Trans. Storage",
            "tcad": "{IEEE} Trans. Comput. Aided Des. Integr. Circuits Syst.",
            "tc": "{IEEE} Trans. Computers",
            "tpds": "{IEEE} Trans. Parallel Distributed Syst.",
            "taco": "{ACM} Trans. Archit. Code Optim.",
            "taas": "{ACM} Trans. Auton. Adapt. Syst.",
            "todaes": "{ACM} Trans. Design Autom. Electr. Syst.",
            "tecs": "{ACM} Trans. Embed. Comput. Syst.",
            "trets": "{ACM} Trans. Reconfigurable Technol. Syst.",
            "tvlsi": "{IEEE} Trans. Very Large Scale Integr. Syst.",
            "jpdc": "J. Parallel Distributed Comput.",
            "jsa": "J. Syst. Archit.",
            "pc": "Parallel Comput.",
            "pe": "Perform. Evaluation",
            "jetc": "{ACM} J. Emerg. Technol. Comput. Syst.",
            "concurrency": "Concurr. Comput. Pract. Exp.",
            "dc": "Distributed Comput.",
            "fgcs": "Future Gener. Comput. Syst.",
            "tcc": "{IEEE} Trans. Cloud Comput.",
            "integration": "Integr.",
            "et": "J. Electron. Test.",
            "grid": "J. Grid Comput.",
            "mam": "Microprocess. Microsystems",
            "rts": "Real Time Syst.",
            "tjs": "J. Supercomput.",
            "tcasI": "{IEEE} Trans. Circuits Syst. I Regul. Pap.",
            "ccfthpc": "{CCF} Trans. High Perform. Comput.",
            "tsusc": "{IEEE} Trans. Sustain. Comput.",
            "jsac": "{IEEE} J. Sel. Areas Commun.",
            "tmc": "{IEEE} Trans. Mob. Comput.",
            "ton": "{IEEE/ACM} Trans. Netw.",
            "toit": "{ACM} Trans. Internet Techn.",
            "tomccap": "{ACM} Trans. Multim. Comput. Commun. Appl.",
            "tosn": "{ACM} Trans. Sens. Networks",
            "cn": "Comput. Networks",
            "tcom": "{IEEE} Trans. Commun.",
            "twc": "{IEEE} Trans. Wirel. Commun.",
            "adhoc": "Elsevier Ad Hoc Networks,",
            "comcom": "Comput. Commun.",
            "tnsm": "{IEEE} Trans. Netw. Serv. Manag.",
            "iet-com": "{IET} Commun.",
            "jnca": "J. Netw. Comput. Appl.",
            "monet": "Mob. Networks Appl.",
            "networks": "Wiley Networks",
            "ppna": "Peer Peer Netw. Appl.",
            "wicomm": "Wirel. Commun. Mob. Comput.",
            "winet": "Wirel. Networks",
            "iot": "Internet Things",
            "tdsc": "{IEEE} Trans. Dependable Secur. Comput.",
            "tifs": "{IEEE} Trans. Inf. Forensics Secur.",
            "joc": "J. Cryptol.",
            "tissec": "{ACM} Trans. Priv. Secur.",
            "compsec": "Comput. Secur.",
            "dcc": "Des. Codes Cryptogr.",
            "jcs": "J. Comput. Secur.",
            "clsr": "Comput. Law Secur. Rev.",
            "ejisec": "{EURASIP} J. Inf. Secur.",
            "iet-ifs": "{IET} Inf. Secur.",
            "imcs": "Inf. Comput. Secur.",
            "ijics": "Int. J. Inf. Comput. Secur.",
            "ijisp": "Int. J. Inf. Secur. Priv.",
            "istr": "J. Inf. Secur. Appl.",
            "scn": "Secur. Commun. Networks",
            "cybersec": "Cybersecur.",
            "toplas": "{ACM} Trans. Program. Lang. Syst.",
            "tosem": "{ACM} Trans. Softw. Eng. Methodol.",
            "tse": "{IEEE} Trans. Software Eng.",
            "tsc": "{IEEE} Trans. Serv. Comput.",
            "ase": "Autom. Softw. Eng.",
            "ese": "Empir. Softw. Eng.",
            "iet-sen": "{IET} Softw.",
            "infsof": "Inf. Softw. Technol.",
            "jfp": "J. Funct. Program.",
            "smr": "J. Softw. Evol. Process.",
            "jss": "J. Syst. Softw.",
            "re": "Requir. Eng.",
            "scp": "Sci. Comput. Program.",
            "sosym": "Softw. Syst. Model.",
            "stvr": "Softw. Test. Verification Reliab.",
            "spe": "Softw. Pract. Exp.",
            "cl": "Comput. Lang. Syst. Struct.",
            "ijseke": "Int. J. Softw. Eng. Knowl. Eng.",
            "sttt": "Int. J. Softw. Tools Technol. Transf.",
            "jlap": "J. Log. Algebraic Methods Program.",
            "jwe": "J. Web Eng.",
            "soca": "Serv. Oriented Comput. Appl.",
            "sqj": "Softw. Qual. J.",
            "tplp": "Theory Pract. Log. Program.",
            "pacmpl": "Proc. {ACM} Program. Lang.",
            "tods": "{ACM} Trans. Database Syst.",
            "tois": "{ACM} Trans. Inf. Syst.",
            "tkde": "{IEEE} Trans. Knowl. Data Eng.",
            "vldb": "{VLDB} J.",
            "tkdd": "{ACM} Trans. Knowl. Discov. Data",
            "tweb": "{ACM} Trans. Web",
            "aei": "Adv. Eng. Informatics",
            "dke": "Data Knowl. Eng.",
            "datamine": "Data Min. Knowl. Discov.",
            "ejis": "Eur. J. Inf. Syst.",
            "geoinformatica": "Springer GeoInformatica",
            "ipm": "Inf. Process. Manag.",
            "isci": "Inf. Sci.",
            "is": "Inf. Syst.",
            "jasis": "J. Assoc. Inf. Sci. Technol.",
            "ws": "J. Web Semant.",
            "kais": "Knowl. Inf. Syst.",
            "dpd": "Distributed Parallel Databases",
            "iam": "Inf. Manag.",
            "ipl": "Inf. Process. Lett.",
            "ir": "Discov. Comput.",
            "ijcis": "Int. J. Cooperative Inf. Syst.",
            "gis": "Int. J. Geogr. Inf. Sci.",
            "ijis": "Int. J. Intell. Syst.",
            "ijkm": "Int. J. Knowl. Manag.",
            "ijswis": "Int. J. Semantic Web Inf. Syst.",
            "jcis": "J. Comput. Inf. Syst.",
            "jdm": "J. Database Manag.",
            "jgim": "J. Glob. Inf. Manag.",
            "jiis": "J. Intell. Inf. Syst.",
            "jsis": "J. Strateg. Inf. Syst.",
            "dase": "Data Sci. Eng.",
            "tit": "{IEEE} Trans. Inf. Theory",
            "iandc": "Inf. Comput.",
            "siamcomp": "{SIAM} J. Comput.",
            "talg": "{ACM} Trans. Algorithms",
            "tocl": "{ACM} Trans. Comput. Log.",
            "toms": "{ACM} Trans. Math. Softw.",
            "algorithmica": "Springer Algorithmica",
            "cc": "Comput. Complex.",
            "fac": "Formal Aspects Comput.",
            "fmsd": "Formal Methods Syst. Des.",
            "informs": "{INFORMS} J. Comput.",
            "jcss": "J. Comput. Syst. Sci.",
            "jgo": "J. Glob. Optim.",
            "jsc": "J. Symb. Comput.",
            "mscs": "Math. Struct. Comput. Sci.",
            "tcs": "Theor. Comput. Sci.",
            "acta": "Springer Acta Informatica",
            "apal": "Ann. Pure Appl. Log.",
            "dam": "Discret. Appl. Math.",
            "fuin": "Fundam. Informaticae",
            "lisp": "High. Order Symb. Comput.",
            "ipl": "Inf. Process. Lett.",
            "jc": "J. Complex.",
            "logcom": "J. Log. Comput.",
            "jsyml": "J. Symb. Log.",
            "lmcs": "Log. Methods Comput. Sci.",
            "siamdm": "{SIAM} J. Discret. Math.",
            "mst": "Theory Comput. Syst.",
            "tog": "{ACM} Trans. Graph.",
            "tip": "{IEEE} Trans. Image Process.",
            "tvcg": "{IEEE} Trans. Vis. Comput. Graph.",
            "tomccap": "{ACM} Trans. Multim. Comput. Commun. Appl.",
            "cagd": "Comput. Aided Geom. Des.",
            "cgf": "Comput. Graph. Forum",
            "cad": "Comput. Aided Des.",
            "cvgip": "Graph. Model.",
            "tcsv": "{IEEE} Trans. Circuits Syst. Video Technol.",
            "tmm": "{IEEE} Trans. Multim.",
            "siamis": "{SIAM} J. Imaging Sci.",
            "speech": "Speech Commun.",
            "comgeo": "Comput. Geom.",
            "jvca": "Comput. Animat. Virtual Worlds",
            "cg": "Comput. Graph.",
            "dcg": "Discret. Comput. Geom.",
            "spl": "{IEEE} Signal Process. Lett.",
            "iet-ipr": "{IET} Image Process.",
            "jvcir": "J. Vis. Commun. Image Represent.",
            "mms": "Multim. Syst.",
            "mta": "Multim. Tools Appl.",
            "sigpro": "Signal Process.",
            "spic": "Signal Process. Image Commun.",
            "vc": "Vis. Comput.",
            "cvm": "Comput. Vis. Media",
            "ai": "Artif. Intell.",
            "pami": "{IEEE} Trans. Pattern Anal. Mach. Intell.",
            "ijcv": "Int. J. Comput. Vis.",
            "jmlr": "J. Mach. Learn. Res.",
            "tap": "{ACM} Trans. Appl. Percept.",
            "tslp": "{ACM} Trans. Speech Lang. Process.",
            "aamas": "Auton. Agents Multi Agent Syst.",
            "coling": "Comput. Linguistics",
            "cviu": "Comput. Vis. Image Underst.",
            "dke": "Data Knowl. Eng.",
            "ec": "Evol. Comput.",
            "taffco": "{IEEE} Trans. Affect. Comput.",
            "taslp": "{IEEE} {ACM} Trans. Audio Speech Lang. Process.",
            "tcyb": "{IEEE} Trans. Cybern.",
            "tec": "{IEEE} Trans. Evol. Comput.",
            "tfs": "{IEEE} Trans. Fuzzy Syst.",
            "tnn": "{IEEE} Trans. Neural Networks Learn. Syst.",
            "ijar": "Int. J. Approx. Reason.",
            "jair": "J. Artif. Intell. Res.",
            "jar": "J. Autom. Reason.",
            "ml": "Mach. Learn.",
            "neco": "Neural Comput.",
            "nn": "Elsevier Neural Networks",
            "tacl": "Trans. Assoc. Comput. Linguistics",
            "talip": "{ACM} Trans. Asian Low Resour. Lang. Inf. Process.",
            "apin": "Appl. Intell.",
            "artmed": "Artif. Intell. Medicine",
            "alife": "Artif. Life",
            "ci": "Comput. Intell.",
            "csl": "Comput. Speech Lang.",
            "connection": "Connect. Sci.",
            "dss": "Decis. Support Syst.",
            "eaai": "Eng. Appl. Artif. Intell.",
            "es": "Expert Syst. J. Knowl. Eng.",
            "eswa": "Expert Syst. Appl.",
            "fss": "Fuzzy Sets Syst.",
            "tciaig": "{IEEE} Trans. Games",
            "iet-cvi": "{IET} Comput. Vis.",
            "iet-spr": "{IET} Signal Process.",
            "ivc": "Image Vis. Comput.",
            "ida": "Intell. Data Anal.",
            "ijcia": "Int. J. Comput. Intell. Appl.",
            "ijis": "Int. J. Intell. Syst.",
            "ijns": "Int. J. Neural Syst.",
            "ijprai": "Int. J. Pattern Recognit. Artif. Intell.",
            "ijufks": "Int. J. Uncertain. Fuzziness Knowl. Based Syst.",
            "ijdar": "Int. J. Document Anal. Recognit.",
            "jetai": "J. Exp. Theor. Artif. Intell.",
            "kbs": "Knowl. Based Syst.",
            "mt": "Mach. Transl.",
            "mva": "Mach. Vis. Appl.",
            "nc": "Nat. Comput.",
            "nle": "Nat. Lang. Eng.",
            "nca": "Neural Comput. Appl.",
            "npl": "Neural Process. Lett.",
            "ijon": "Elsevier Neurocomputing",
            "paa": "Pattern Anal. Appl.",
            "prl": "Pattern Recognit. Lett.",
            "soco": "Soft Comput.",
            "wias": "Web Intell.",
            "tiis": "{ACM} Trans. Interact. Intell. Syst.",
            "tochi": "{ACM} Trans. Comput. Hum. Interact.",
            "ijmms": "Int. J. Hum. Comput. Stud.",
            "cscw": "Comput. Support. Cooperative Work.",
            "hhci": "Hum. Comput. Interact.",
            "thms": "{IEEE} Trans. Hum. Mach. Syst.",
            "iwc": "Interact. Comput.",
            "ijhci": "Int. J. Hum. Comput. Interact.",
            "umuai": "User Model. User Adapt. Interact.",
            "tsmc": "{IEEE} Trans. Syst. Man Cybern. Syst.",
            "behaviourIT": "Behav. Inf. Technol.",
            "puc": "Pers. Ubiquitous Comput.",
            "percom": "Pervasive Mob. Comput.",
            "pacmhci": "Proc. {ACM} Hum. Comput. Interact.",
            "jacm": "J. ACM",
            "pieee": "Proc. IEEE",
            "chinaf": "Sci. China Inf. Sci.",
            "bioinformatics": "Bioinform.",
            "bib": "Briefings Bioinform.",
            "tase": "{IEEE} Trans Autom. Sci. Eng.",
            "tgrs": "{IEEE} Trans. Geosci. Remote. Sens.",
            "tits": "{IEEE} Trans. Intell. Transp. Syst.",
            "tmi": "{IEEE} Trans. Medical Imaging",
            "trob": "{IEEE} Trans. Robotics",
            "tcbb": "{IEEE} {ACM} Trans. Comput. Biol. Bioinform.",
            "jcst": "J. Comput. Sci. Technol.",
            "jamia": "J. Am. Medical Informatics Assoc.",
            "ploscb": "PLoS Comput. Biol.",
            "cj": "Comput. J.",
            "www": "Springer World Wide Web",
            "fcsc": "Frontiers Comput. Sci.",
            "bmcbi": "{BMC} Bioinform.",
            "cas": "Cybern. Syst.",
            "lgrs": "{IEEE} Geosci. Remote. Sens. Lett.",
            "titb": "{IEEE} J. Biomed. Health Informatics",
            "tbd": "{IEEE} Trans. Big Data",
            "jbi": "J. Biomed. Informatics",
            "mia": "Medical Image Anal.",
            "tii": "{IEEE} Trans. Ind. Informatics",
            "tcps": "{ACM} Trans. Cyber Phys. Syst.",
            "jeric": "{ACM} Trans. Comput. Educ.",
            "jzusc": "Frontiers Inf. Technol. Electron. Eng.",
            "tcss": "{IEEE} Trans. Comput. Soc. Syst.",
            "tr": "{IEEE} Trans. Reliab.",
            "imwut": "Proc. {ACM} Interact. Mob. Wearable Ubiquitous Technol."
            },
        PubType.ARXIV: {
            'corr': 'CoRR',
            }
        }
