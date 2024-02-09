import json
import requests

from enum import Enum


# Funzione per convertire le stringhe in enum
def convert_to_enum(value, enum):
    for e in enum:
        if e.value == value:
            return e
    return None

# Classe per deserializzare i dati
class ConfigMCA:
        
    # Definizione degli enum come specificato
    class TriggerMode(Enum):
        INTERNAL = "internal"
        EXTERNAL = "external"
        LOGIC_OR = "logic_or"
        LOGIC_AND = "logic_and"

    class TriggerType(Enum):
        FAST_TRAPEZOIDAL = "ft"
        LEADING_EDGE = "le"

    class Polarity(Enum):
        NEGATIVE = "negative"
        POSITIVE = "positive"

    class EnergyMode(Enum):
        TRAPEZOIDAL = "trap"
        QDC = "qdc"
        PEAK_HOLDER = "peak"

    class BaselineMode(Enum):
        BASELINE_SHAPER = "baseline_restorer"
        MOVING_AVERAGE = "moving_average"

    class TrapPurMode(Enum):
        NO_PUR = "no_pur"
        SIMPLE_PUR = "simple_pur"
        ADVANCED_PUR = "advanced_pur"
        
    def __init__(self, config):
        self.baseline_hold = 10
        self.baseline_len = 10
        self.baseline_mode =  ConfigMCA.BaselineMode.BASELINE_SHAPER
        self.energy_mode = ConfigMCA.EnergyMode.QDC
        self.ft_flat = 1
        self.ft_offset = 0
        self.ft_polarity = ConfigMCA.Polarity.POSITIVE
        self.ft_shaping = 10
        self.ft_tau = 1
        self.ft_threshold = 10
        self.le_delta = 30
        self.le_inib = 25
        self.le_polarity =  ConfigMCA.Polarity.POSITIVE
        self.le_threshold =1000
        self.peak_pileup = 0
        self.peak_sampling = 0
        self.qdc_post_inibit = 100
        self.qdc_pre = config["qdc_pre"]
        self.qdc_qlong = 100
        self.qdc_qshort = 20
        self.risetime_pre = 0
        self.risetime_start = 0
        self.risetime_stop = 0
        self.risetime_window = 0
        self.trap_flat = 0
        self.trap_gain = 1
        self.trap_offset = 0
        self.trap_pileupinib = 10
        self.trap_polarity = ConfigMCA.Polarity.POSITIVE
        self.trap_pur_mode = ConfigMCA.TrapPurMode.SIMPLE_PUR
        self.trap_sampling = 0
        self.trap_shaping = 0
        self.trap_tau = 0
        self.trigger_mode = ConfigMCA.TriggerMode.INTERNAL 
        self.trigger_type = ConfigMCA.TriggerType.LEADING_EDGE
        
    def process_config_json(self, config):
        self.baseline_hold = config["baseline_hold"]
        self.baseline_len = config["baseline_len"]
        self.baseline_mode = convert_to_enum(config["baseline_mode"], ConfigMCA.BaselineMode)
        self.energy_mode = convert_to_enum(config["energy_mode"], ConfigMCA.EnergyMode)
        self.ft_flat = config["ft_flat"]
        self.ft_offset = config["ft_offset"]
        self.ft_polarity = convert_to_enum(config["ft_polarity"], ConfigMCA.Polarity)
        self.ft_shaping = config["ft_shaping"]
        self.ft_tau = config["ft_tau"]
        self.ft_threshold = config["ft_threshold"]
        self.le_delta = config["le_delta"]
        self.le_inib = config["le_inib"]
        self.le_polarity = convert_to_enum(config["le_polarity"], ConfigMCA.Polarity)
        self.le_threshold = config["le_threshold"]
        self.peak_pileup = config["peak_pileup"]
        self.peak_sampling = config["peak_sampling"]
        self.qdc_post_inibit = config["qdc_post_inibit"]
        self.qdc_pre = config["qdc_pre"]
        self.qdc_qlong = config["qdc_qlong"]
        self.qdc_qshort = config["qdc_qshort"]
        self.risetime_pre = config["risetime_pre"]
        self.risetime_start = config["risetime_start"]
        self.risetime_stop = config["risetime_stop"]
        self.risetime_window = config["risetime_window"]
        self.trap_flat = config["trap_flat"]
        self.trap_gain = config["trap_gain"]
        self.trap_offset = config["trap_offset"]
        self.trap_pileupinib = config["trap_pileupinib"]
        self.trap_polarity = convert_to_enum(config["trap_polarity"], ConfigMCA.Polarity)
        self.trap_pur_mode = convert_to_enum(config["trap_pur_mode"], ConfigMCA.TrapPurMode)
        self.trap_sampling = config["trap_sampling"]
        self.trap_shaping = config["trap_shaping"]
        self.trap_tau = config["trap_tau"]
        self.trigger_mode = convert_to_enum(config["trigger_mode"], ConfigMCA.TriggerMode)
        self.trigger_type = convert_to_enum(config["trigger_type"], ConfigMCA.TriggerType)

    def to_json(self):
        return {
            "baseline_hold": self.baseline_hold,
            "baseline_len": self.baseline_len,
            "baseline_mode": self.baseline_mode.value,
            "energy_mode": self.energy_mode.value,
            "ft_flat": self.ft_flat,
            "ft_offset": self.ft_offset,
            "ft_polarity": self.ft_polarity.value,
            "ft_shaping": self.ft_shaping,
            "ft_tau": self.ft_tau,
            "ft_threshold": self.ft_threshold,
            "le_delta": self.le_delta,
            "le_inib": self.le_inib,
            "le_polarity": self.le_polarity.value,
            "le_threshold": self.le_threshold,
            "peak_pileup": self.peak_pileup,
            "peak_sampling": self.peak_sampling,
            "qdc_post_inibit": self.qdc_post_inibit,
            "qdc_pre": self.qdc_pre,
            "qdc_qlong": self.qdc_qlong,
            "qdc_qshort": self.qdc_qshort,
            "risetime_pre": self.risetime_pre,
            "risetime_start": self.risetime_start,
            "risetime_stop": self.risetime_stop,
            "risetime_window": self.risetime_window,
            "trap_flat": self.trap_flat,
            "trap_gain": self.trap_gain,
            "trap_offset": self.trap_offset,
            "trap_pileupinib": self.trap_pileupinib,
            "trap_polarity": self.trap_polarity.value,
            "trap_pur_mode": self.trap_pur_mode.value,
            "trap_sampling": self.trap_sampling,
            "trap_shaping": self.trap_shaping,
            "trap_tau": self.trap_tau,
            "trigger_mode": self.trigger_mode.value,
            "trigger_type": self.trigger_type.value
        }
        
    def __str__(self):
        properties = vars(self)
        return '\n'.join([f'{key}: {value}' for key, value in properties.items() if key.startswith('_')])
    
    @property
    def baseline_hold(self):
        return self._baseline_hold
    
    @baseline_hold.setter
    def baseline_hold(self, value):
        self._baseline_hold = value
    
    @property
    def baseline_len(self):
        return self._baseline_len
    
    @baseline_len.setter
    def baseline_len(self, value):
        self._baseline_len = value
    
    @property
    def baseline_mode(self):
        return self._baseline_mode
    
    @baseline_mode.setter
    def baseline_mode(self, value):
        self._baseline_mode = value
    
    @property
    def energy_mode(self):
        return self._energy_mode
    
    @energy_mode.setter
    def energy_mode(self, value):
        self._energy_mode = value
    
    @property
    def ft_flat(self):
        return self._ft_flat
    
    @ft_flat.setter
    def ft_flat(self, value):
        self._ft_flat = value
    
    @property
    def ft_offset(self):
        return self._ft_offset
    
    @ft_offset.setter
    def ft_offset(self, value):
        self._ft_offset = value
    
    @property
    def ft_polarity(self):
        return self._ft_polarity
    
    @ft_polarity.setter
    def ft_polarity(self, value):
        self._ft_polarity = value
    
    @property
    def ft_shaping(self):
        return self._ft_shaping
    
    @ft_shaping.setter
    def ft_shaping(self, value):
        self._ft_shaping = value
    
    @property
    def ft_tau(self):
        return self._ft_tau
    
    @ft_tau.setter
    def ft_tau(self, value):
        self._ft_tau = value
    
    @property
    def ft_threshold(self):
        return self._ft_threshold
    
    @ft_threshold.setter
    def ft_threshold(self, value):
        self._ft_threshold = value
    
    @property
    def le_delta(self):
        return self._le_delta
    
    @le_delta.setter
    def le_delta(self, value):
        self._le_delta = value
    
    @property
    def le_inib(self):
        return self._le_inib
    
    @le_inib.setter
    def le_inib(self, value):
        self._le_inib = value
    
    @property
    def le_polarity(self):
        return self._le_polarity
    
    @le_polarity.setter
    def le_polarity(self, value):
        self._le_polarity = value
    
    @property
    def le_threshold(self):
        return self._le_threshold
    
    @le_threshold.setter
    def le_threshold(self, value):
        self._le_threshold = value
    
    @property
    def peak_pileup(self):
        return self._peak_pileup
    
    @peak_pileup.setter
    def peak_pileup(self, value):
        self._peak_pileup = value
    
    @property
    def peak_sampling(self):
        return self._peak_sampling
    
    @peak_sampling.setter
    def peak_sampling(self, value):
        self._peak_sampling = value
    
    @property
    def qdc_post_inibit(self):
        return self._qdc_post_inibit
    
    @qdc_post_inibit.setter
    def qdc_post_inibit(self, value):
        self._qdc_post_inibit = value
    
    @property
    def qdc_pre(self):
        return self._qdc_pre
    
    @qdc_pre.setter
    def qdc_pre(self, value):
        self._qdc_pre = value
    
    @property
    def qdc_qlong(self):
        return self._qdc_qlong
    
    @qdc_qlong.setter
    def qdc_qlong(self, value):
        self._qdc_qlong = value
    
    @property
    def qdc_qshort(self):
        return self._qdc_qshort
    
    @qdc_qshort.setter
    def qdc_qshort(self, value):
        self._qdc_qshort = value
    
    @property
    def risetime_pre(self):
        return self._risetime_pre
    
    @risetime_pre.setter
    def risetime_pre(self, value):
        self._risetime_pre = value
    
    @property
    def risetime_start(self):
        return self._risetime_start
    
    @risetime_start.setter
    def risetime_start(self, value):
        self._risetime_start = value
    
    @property
    def risetime_stop(self):
        return self._risetime_stop
    
    @risetime_stop.setter
    def risetime_stop(self, value):
        self._risetime_stop = value
    
    @property
    def risetime_window(self):
        return self._risetime_window
    
    @risetime_window.setter
    def risetime_window(self, value):
        self._risetime_window = value
    
    @property
    def trap_flat(self):
        return self._trap_flat
    
    @trap_flat.setter
    def trap_flat(self, value):
        self._trap_flat = value
    
    @property
    def trap_gain(self):
        return self._trap_gain
    
    @trap_gain.setter
    def trap_gain(self, value):
        self._trap_gain = value
    
    @property
    def trap_offset(self):
        return self._trap_offset
    
    @trap_offset.setter
    def trap_offset(self, value):
        self._trap_offset = value
    
    @property
    def trap_pileupinib(self):
        return self._trap_pileupinib
    
    @trap_pileupinib.setter
    def trap_pileupinib(self, value):
        self._trap_pileupinib = value
    
    @property
    def trap_polarity(self):
        return self._trap_polarity
    
    @trap_polarity.setter
    def trap_polarity(self, value):
        self._trap_polarity = value
    
    @property
    def trap_pur_mode(self):
        return self._trap_pur_mode
    
    @trap_pur_mode.setter
    def trap_pur_mode(self, value):
        self._trap_pur_mode = value
    
    @property
    def trap_sampling(self):
        return self._trap_sampling
    
    @trap_sampling.setter
    def trap_sampling(self, value):
        self._trap_sampling = value
    
    @property
    def trap_shaping(self):
        return self._trap_shaping
    
    @trap_shaping.setter
    def trap_shaping(self, value):
        self._trap_shaping = value
    
    @property
    def trap_tau(self):
        return self._trap_tau
    
    @trap_tau.setter
    def trap_tau(self, value):
        self._trap_tau = value
    
    @property
    def trigger_mode(self):
        return self._trigger_mode
    
    @trigger_mode.setter
    def trigger_mode(self, value):
        self._trigger_mode = value
    
    @property
    def trigger_type(self):
        return self._trigger_type
    
    @trigger_type.setter
    def trigger_type(self, value):
        self._trigger_type = value


class Polarity(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"

class AnalogOut(Enum):
    ENERGY_FILTER_OUTPUT = "energy_filter_output"
    # Assumo altri valori possibili qui, aggiungili secondo necessità

class DigitalIn(Enum):
    EXTERNAL_TRIGGER = "external_trigger"
    # Assumo altri valori possibili qui, aggiungili secondo necessità

class DigitalOut(Enum):
    TRIGGER = "trigger"
    # Assumo altri valori possibili qui, aggiungili secondo necessità

# Classe per la conversione e gestione dei valori
class ConfigIO:
    def __init__(self, config):
        self.analog_in_polarity = config.get("analog_in_polarity", Polarity.POSITIVE.value)
        self.analog_out = config.get("analog_out", AnalogOut.ENERGY_FILTER_OUTPUT.value)
        self.digital_in = config.get("digital_in", DigitalIn.EXTERNAL_TRIGGER.value)
        self.digital_out = config.get("digital_out", DigitalOut.TRIGGER.value)
        
    def __str__(self):
        properties = vars(self)
        return '\n'.join([f'{key}: {value}' for key, value in properties.items() if key.startswith('_')])
    
    @property
    def analog_in_polarity(self):
        return self._analog_in_polarity

    @analog_in_polarity.setter
    def analog_in_polarity(self, value):
        self._analog_in_polarity = convert_to_enum(value, Polarity)

    @property
    def analog_out(self):
        return self._analog_out

    @analog_out.setter
    def analog_out(self, value):
        self._analog_out = convert_to_enum(value, AnalogOut)

    @property
    def digital_in(self):
        return self._digital_in

    @digital_in.setter
    def digital_in(self, value):
        self._digital_in = convert_to_enum(value, DigitalIn)

    @property
    def digital_out(self):
        return self._digital_out

    @digital_out.setter
    def digital_out(self, value):
        self._digital_out = convert_to_enum(value, DigitalOut)


class SmartMCA:
    url = ""  
    connected = False  
    cookie = None
    _API_PATH_ = "/mca/api"
    def __init__(self) -> None:
        url = ""
        
        
    def connect(self, url, username, password):
        self.url = url
        #post username and passowrd in a form format to the url /login
        #if the response is 200, then set connected to True
        #else set connected to False
        data = {
            "username": username,
            "password": password
        }
        
        response = requests.post(self.url + "/api/login", json=data)
        
        if json.loads(response.text)["success"] == True:
            self.connected = True
            #store the cookie in a variable
            self.cookie = response.cookies
        else:
            self.connected = False

        
    
    def disconnect(self):
        self.connected = False
        self.cookie = None
        return self.connected
    
    def http_get(self, url):
        if not self.connected:
            raise Exception("Not connected to the server", 1)
        response = requests.get(self.url + url, cookies=self.cookie)
        if response.status_code != 200:
            raise Exception("Error in getting server status", 2)
        
        j = response.json()
        
        return j
        
    
    def http_post(self, url, data):
        if not self.connected:
            raise Exception("Not connected to the server", 1)
        response = requests.post(self.url + url, cookies=self.cookie, json=data)
        if response.status_code != 200:
            raise Exception("Error in getting server status", 2)    
        return response.json()
    
    def get_server_status(self):
        j = self.http_get(self._API_PATH_ + "/get_server_status")
        return j["status"]
        
    def get_mca_configuration(self):
        j = self.http_get(self._API_PATH_ + "/HLL/hl_get_processing_param")
        config = ConfigMCA(j)
        config.process_config_json(j)
        return config
    
    def set_mca_configuration(self, config):
        j = config.to_json()
        r = self.http_post(self._API_PATH_ + "/HLL/hl_set_processing_param", j)
        if r["result"] != "ok":
            raise Exception(r["error"], 3)
    
    def get_io_configuration(self):
        j = self.http_get(self._API_PATH_ + "/HLL/hl_get_processing_param")
        config = ConfigIO(j)
        config.process_config_json(j)
        return config
    
    def set_io_configuration(self, config):
        j = config.to_json()
        r = self.http_post(self._API_PATH_ + "/HLL/hl_set_processing_param", j)
        if r["result"] != "ok":
            raise Exception(r["error"], 3)