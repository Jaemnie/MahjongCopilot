"""Language string constants"""

class LanStr:
    """ String constants for default language (English) """
    LANGUAGE_NAME = 'English'

    # GUI
    APP_TITLE = 'Mahjong Copilot'
    START_BROWSER = "Start Web Client"
    WEB_OVERLAY = "Overlay"
    AUTOPLAY = "Autoplay"
    AUTO_JOIN_GAME = "Auto Join"
    AUTO_JOIN_TIMER = "Auto Join Timer"
    OPEN_LOG_FILE = "Open Log File"
    SETTINGS = "Settings"
    HELP = "Help"
    LOADING = "Loading..."
    EXIT = "Exit"
    EIXT_CONFIRM = "Are you sure you want to exit?"
    AI_OUTPUT = 'AI Guidance'
    GAME_INFO = 'Game Info'    
    ON = "On"
    OFF = "Off"
    
    # help
    DOWNLOAD_UPDATE = "Download Update"
    START_UPDATE = "Update & Restart"
    CHECK_FOR_UPDATE = "Check Update"
    CHECKING_UPDATE = "Checking for new update..."
    UPDATE_AVAILABLE = "New update available"
    NO_UPDATE_FOUND = "No new update found"
    DOWNLOADING = "Downloading..."
    UNZIPPING = "Unzipping..."
    UPDATE_PREPARED = "Update prepared. Click the button to update and restart."

    ### Settings
    SAVE = "Save"
    CANCEL = "Cancel"
    SETTINGS_TIPS = "A restart is needed to apply MITM related settings"
    AUTO_LAUNCH_BROWSER = "Auto Launch Browser"
    MITM_PORT = "MITM Server Port"
    UPSTREAM_PROXY = "Upstream Proxy"
    CLIENT_SIZE = "Client Size"
    MAJSOUL_URL = "Majsoul URL"
    ENABLE_CHROME_EXT = "Enable Chrome Extensions"
    LANGUAGE = "Display Language"
    CLIENT_INJECT_PROXY = "Auto Proxy Majsoul Windows Client"
    MODEL_TYPE = "AI Model Type"
    AI_MODEL_FILE = "Local Model File (4P)"
    AI_MODEL_FILE_3P = "Local Model File (3P)"
    AKAGI_OT_URL = "AkagiOT Server URL"
    AKAGI_OT_APIKEY = "AkagiOT API Key"
    MJAPI_URL = "MJAPI Server URL"
    MJAPI_USER = "MJAPI User"
    MJAPI_USAGE = "API Usage"
    MJAPI_SECRET = "MJAPI Secret"
    MJAPI_MODEL_SELECT = "MJAPI Model Select"
    LOGIN_TO_REFRESH = "Log in to refresh"
    MITM_PORT_ERROR_PROMPT = "Invalid MITM Port (must between 1000~65535)"
    # autoplay
    AUTO_PLAY_SETTINGS = "Autoplay Settings"
    AUTO_IDLE_MOVE = "Idle Mouse Move"
    DRAG_DAHAI = "Mouse drag dahai"
    RANDOM_CHOICE = "Randomize AI Choice"
    REPLY_EMOJI_CHANCE = "Reply Emoji Rate"
    RANDOM_DELAY_RANGE = "Base Delay Range (sec)"    
    GAME_LEVELS = ["Bronze", "Silver", "Gold", "Jade", "Throne"]
    GAME_MODES = ["4-P East","4-P South","3-P East","3-P South"]
    MOUSE_RANDOM_MOVE = "Randomize Move"
    
    # Status
    MAIN_THREAD  = "Main Thread"
    MITM_SERVICE = "MITM Service"
    BROWSER = "Browser"
    PROXY_CLIENT = "Proxy Client"
    GAME_RUNNING = "Game Running"
    GAME_ERROR = "Game Error!"
    SYNCING = "Syncing..."
    CALCULATING = "Calculating..."
    READY_FOR_GAME = "Ready"
    GAME_STARTING = "Game Starting"
    KYOKU = "Kyoku"
    HONBA = "Honba"
    MODEL = "Model"
    MODEL_NOT_LOADED = "Model not loaded"
    MODEL_LOADING = "Loading Model..."
    MAIN_MENU = "Main Menu"
    GAME_ENDING = "Game Ending"
    GAME_NOT_RUNNING = "Not Launched"
    # errors
    LOCAL_MODEL_ERROR = "Local Model Loading Error!"
    MITM_SERVER_ERROR = "MITM Service Error!"
    MITM_CERT_NOT_INSTALLED = "Run as admin or manually install MITM cert."
    MAIN_THREAD_ERROR = "Main Thread Error!"
    MODEL_NOT_SUPPORT_MODE_ERROR = "Model not supporting game mode"
    CONNECTION_ERROR = "Network Connection Error"
    BROWSER_ZOOM_OFF = r"Set Browser Zoom level to 100% !"
    CHECK_ZOOM = "Browser Zoom!"
    # Reaction/Actions
    PASS = "Skip"
    DISCARD = "Discard"
    CHI = "Chi"
    PON = "Pon"
    KAN = "Kan"
    KAKAN = "Kakan"
    DAIMINKAN = "Daiminkan"
    ANKAN = "Ankan"
    RIICHI = "Riichi"
    AGARI = "Agari"
    TSUMO = "Tsumo"
    RON = "Ron"
    RYUKYOKU = "Ryukyoku"
    NUKIDORA = "Nukidora"
    OPTIONS_TITLE = "Options:"    
    
    MJAI_2_STR = {
        '1m': '1 Man', '2m': '2 Man', '3m': '3 Man', '4m': '4 Man', '5m': '5 Man',
        '6m': '6 Man', '7m': '7 Man', '8m': '8 Man', '9m': '9 Man',
        '1p': '1 Pin', '2p': '2 Pin', '3p': '3 Pin', '4p': '4 Pin', '5p': '5 Pin',
        '6p': '6 Pin', '7p': '7 Pin', '8p': '8 Pin', '9p': '9 Pin',
        '1s': '1 Sou', '2s': '2 Sou', '3s': '3 Sou', '4s': '4 Sou', '5s': '5 Sou',
        '6s': '6 Sou', '7s': '7 Sou', '8s': '8 Sou', '9s': '9 Sou',
        'E': 'East', 'S': 'South', 'W': 'West', 'N': 'North',
        'C': 'Chun', 'F': 'Hatsu', 'P': 'Haku',
        '5mr': 'Red 5 Man', '5pr': 'Red 5 Pin', '5sr': 'Red 5 Sou',
        'reach': 'Riichi', 'chi_low': 'Chi Low', 'chi_mid': 'Chi Mid', 'chi_high': 'Chi High', 'pon': 'Pon', 'kan_select':'Kan',
        'hora': 'Agari', 'ryukyoku': 'Ryukyoku', 'none':'Skip', 'nukidora':'Nukidora'
    }
      
    def mjai2str(self, mjai_option:str) -> str:
        """ convert mjai option/tile to string in this language"""    
        if mjai_option not in self.MJAI_2_STR:
            return mjai_option        
        return self.MJAI_2_STR[mjai_option]
    

class LanStrZHS(LanStr):
    """ String constants for Korean (Overwritten from Chinese Simplified)"""
    LANGUAGE_NAME = '한국어'
    
    # GUI
    APP_TITLE = '마작 Copilot'
    START_BROWSER = "웹 클라이언트 시작"
    WEB_OVERLAY = "오버레이"
    AUTOPLAY = "자동 플레이"
    AUTO_JOIN_GAME = "자동 참가"
    AUTO_JOIN_TIMER = "자동 참가 타이머"
    OPEN_LOG_FILE = "로그 파일 열기"
    SETTINGS = "설정"
    HELP = "도움말"
    LOADING = "로딩 중..."
    EXIT = "종료"
    EIXT_CONFIRM = "정말 종료하시겠습니까?"
    AI_OUTPUT = 'AI 안내'
    GAME_INFO = '게임 정보'    
    ON = "켜짐"
    OFF = "꺼짐"
    
    # help
    DOWNLOAD_UPDATE = "업데이트 다운로드"
    START_UPDATE = "업데이트 및 재시작"
    CHECK_FOR_UPDATE = "업데이트 확인"
    CHECKING_UPDATE = "새로운 업데이트 확인 중..."
    UPDATE_AVAILABLE = "새로운 업데이트가 있습니다"
    NO_UPDATE_FOUND = "새로운 업데이트가 없습니다"
    DOWNLOADING = "다운로드 중..."
    UNZIPPING = "압축 해제 중..."
    UPDATE_PREPARED = "업데이트 준비 완료. 버튼을 클릭하여 업데이트하고 재시작하세요."
    
    # Settings
    SAVE = "저장"
    CANCEL = "취소"
    SETTINGS_TIPS = "MITM 관련 설정을 적용하려면 재시작이 필요합니다"
    MITM_PORT = "MITM 서버 포트"
    UPSTREAM_PROXY = "업스트림 프록시"
    CLIENT_SIZE = "클라이언트 크기"
    MAJSOUL_URL = "마주소 URL"
    ENABLE_CHROME_EXT = "크롬 확장 기능 활성화"
    LANGUAGE = "표시 언어"
    CLIENT_INJECT_PROXY = "마주소 Windows 클라이언트 자동 프록시"
    MODEL_TYPE = "AI 모델 유형"
    AI_MODEL_FILE = "로컬 모델 파일 (4인)"
    AI_MODEL_FILE_3P = "로컬 모델 파일 (3인)"
    AKAGI_OT_URL = "AkagiOT 서버 URL"
    AKAGI_OT_APIKEY = "AkagiOT API 키"
    MJAPI_URL = "MJAPI 서버 URL"
    MJAPI_USER = "MJAPI 사용자"
    MJAPI_USAGE = "API 사용량"
    MJAPI_SECRET = "MJAPI 비밀키"
    MJAPI_MODEL_SELECT = "MJAPI 모델 선택"
    LOGIN_TO_REFRESH = "로그인 후 새로고침"
    AUTO_LAUNCH_BROWSER = "브라우저 자동 시작"
    MITM_PORT_ERROR_PROMPT = "잘못된 MITM 포트 (1000~65535 사이여야 합니다)"
    # autoplay
    AUTO_PLAY_SETTINGS = "자동 플레이 설정"
    AUTO_IDLE_MOVE = "마우스 유휴 이동"
    DRAG_DAHAI = "마우스 드래그 다하이"
    RANDOM_CHOICE = "AI 선택 랜덤화"
    REPLY_EMOJI_CHANCE = "이모지 응답 확률"
    RANDOM_DELAY_RANGE = "기본 지연 범위 (초)"    
    GAME_LEVELS = ["동", "은", "금", "옥", "왕좌"]
    GAME_MODES = ["4인 동","4인 남","3인 동","3인 남"]
    MOUSE_RANDOM_MOVE = "마우스 이동 랜덤화"
    
    # Status
    MAIN_THREAD  = "메인 스레드"
    MITM_SERVICE = "MITM 서비스"
    BROWSER = "브라우저"
    PROXY_CLIENT = "프록시 클라이언트"
    GAME_RUNNING = "게임 실행 중"
    GAME_ERROR = "게임 오류!"
    SYNCING = "동기화 중..."
    CALCULATING = "계산 중..."
    READY_FOR_GAME = "준비 완료"
    GAME_STARTING = "게임 시작 중"
    KYOKU = "局"
    HONBA = "本場"
    MODEL = "모델"
    MODEL_NOT_LOADED = "모델이 로드되지 않음"
    MODEL_LOADING = "모델 로딩 중..."
    MAIN_MENU = "메인 메뉴"
    GAME_ENDING = "게임 종료 중"
    GAME_NOT_RUNNING = "실행되지 않음"
    #errors
    LOCAL_MODEL_ERROR = "로컬 모델 로딩 오류!"
    MITM_SERVER_ERROR = "MITM 서비스 오류!"
    MITM_CERT_NOT_INSTALLED = "관리자 권한으로 실행하거나 MITM 인증서를 수동으로 설치하세요."
    MAIN_THREAD_ERROR = "메인 스레드 오류!"
    MODEL_NOT_SUPPORT_MODE_ERROR = "모델이 게임 모드를 지원하지 않음"
    CONNECTION_ERROR = "네트워크 연결 오류"
    BROWSER_ZOOM_OFF = r"브라우저 줌 레벨을 100%로 설정하세요!"
    CHECK_ZOOM = "브라우저 줌 확인!"
    # Reaction/Actions
    PASS = "건너뛰기"
    DISCARD = "버리기"
    CHI = "치"
    PON = "폰"
    KAN = "칸"
    KAKAN = "카칸"
    DAIMINKAN = "다이밍칸"
    ANKAN = "안칸"
    RIICHI = "리치"
    AGARI = "아가리"
    TSUMO = "츠모"
    RON = "론"
    RYUKYOKU = "류큐큐"
    NUKIDORA = "누키도로라"
    OPTIONS_TITLE = "옵션:"    
    
    MJAI_2_STR ={
        '1m': '일만', '2m': '이만', '3m': '삼만', '4m': '사만', '5m': '오만',
        '6m': '육만', '7m': '칠만', '8m': '팔만', '9m': '구만',
        '1p': '일통', '2p': '이통', '3p': '삼통', '4p': '사통', '5p': '오통',
        '6p': '육통', '7p': '칠통', '8p': '팔통', '9p': '구통',
        '1s': '일삭', '2s': '이삭', '3s': '삼삭', '4s': '사삭', '5s': '오삭',
        '6s': '육삭', '7s': '칠삭', '8s': '팔삭', '9s': '구삭',
        'E': '동', 'S': '남', 'W': '서', 'N': '북',
        'C': '중', 'F': '발', 'P': '백',
        '5mr': '적오만', '5pr': '적오통', '5sr': '적오삭', 
        'reach': '리치', 'chi_low': '치-하', 'chi_mid': '치-중', 'chi_high': '치-상', 'pon': '폰', 'kan_select':'칸',
        'hora': '아가리', 'ryukyoku': '류큐큐', 'none': '건너뛰기', 'nukidora':'누키도로라'
    }



LAN_OPTIONS:dict[str, LanStr] = {
    'EN': LanStr(),
    'ZHS': LanStrZHS(), 
}
""" dict of {language code: LanString instance}"""
