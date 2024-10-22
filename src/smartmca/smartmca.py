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
        LOGIC_AND_I_E = "logic_and_i&e"
        LOGIC_AND_NOT_I_E = "logic_and_!i&e"
        LOGIC_AND_I_NOT_E = "logic_and_i&!e"

    class TriggerEdge(Enum):
        RISING = "rising"
        FALLING = "falling"
        BOTH = "both"
    
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
        MOVING_AVERAGE = "moving_average"
        CONSTANT = "constant"
        NONE = "none"

    class PurMode(Enum):
        NO_PUR = "none"
        SINGLE = "single"
        DOUBLE = "double"

    class PurType(Enum):
        PARALYZABLE = "paralyzable"
        NOT_PARALYZABLE = "not_paralyzable"

    class RisetimeMode(Enum):
        TWO_TH = "start_stop"
        THREE_TH = "three_threshold"
        
    class RisetimeAlgorithm(Enum):
        RISETIME = "start_stop"
        RISETIME_LONG = "long"
        RISETIME_SHORT = "short"
    
    def __init__(self):
        self.trigger_mode = ConfigMCA.TriggerMode.INTERNAL 
        self.trigger_type = ConfigMCA.TriggerType.LEADING_EDGE
        self.trigger_edge = ConfigMCA.TriggerEdge.RISING
        self.le_delta = 30
        self.le_inib = 1000
        self.le_polarity =  ConfigMCA.Polarity.POSITIVE
        self.le_threshold =8300
        self.ft_flat = 50
        self.ft_offset = 0
        self.ft_polarity = ConfigMCA.Polarity.POSITIVE
        self.ft_shaping = 250
        self.ft_tau = 1000
        self.ft_threshold = 10
        self.energy_mode = ConfigMCA.EnergyMode.QDC
        self.qdc_post_inibit = 5000
        self.qdc_pre = 100
        self.qdc_qlong = 5000
        self.qdc_qshort = 100
        self.qdc_gain = 3
        self.psd_gain = 3   
        self.trap_flat = 50
        self.trap_gain = 10
        self.trap_sampling = 80
        self.trap_shaping = 500
        self.trap_tau = 1000
        self.peak_pretrigger = 100
        self.peak_sampling = 1000
        self.baseline_hold = 10000
        self.baseline_len = 9
        self.baseline_delay = 0
        self.baseline_mode =  ConfigMCA.BaselineMode.MOVING_AVERAGE
        self.pur_mode = ConfigMCA.PurMode.SINGLE
        self.pur_type = ConfigMCA.PurType.NOT_PARALYZABLE
        self.pur_single_lenght = 2000
        self.pur_double_lenght = 500        
        self.risetime_mode = ConfigMCA.RisetimeMode.TWO_TH
        self.risetime_algorithm = ConfigMCA.RisetimeAlgorithm.RISETIME
        self.risetime_pre = 0
        self.risetime_th1 = 10
        self.risetime_th2 = 90
        self.risetime_th3 = 50        
        self.risetime_window = 2500
        
    def process_config_json(self, config):
        self.trigger_mode = convert_to_enum(config["trigger_mode"], ConfigMCA.TriggerMode)
        self.trigger_type = convert_to_enum(config["trigger_type"], ConfigMCA.TriggerType)
        self.trigger_edge = convert_to_enum(config["trigger_edge"], ConfigMCA.TriggerEdge)
        self.le_delta = config["le_delta"]
        self.le_inib = config["le_inib"]
        self.le_polarity = convert_to_enum(config["le_polarity"], ConfigMCA.Polarity)
        self.le_threshold = config["le_threshold"]
        self.ft_flat = config["ft_flat"]
        self.ft_offset = config["ft_offset"]
        self.ft_polarity = convert_to_enum(config["ft_polarity"], ConfigMCA.Polarity)
        self.ft_shaping = config["ft_shaping"]
        self.ft_tau = config["ft_tau"]
        self.ft_threshold = config["ft_threshold"]
        self.energy_mode = convert_to_enum(config["energy_mode"], ConfigMCA.EnergyMode)
        self.qdc_post_inibit = config["qdc_post_inibit"]
        self.qdc_pre = config["qdc_pre"]
        self.qdc_qlong = config["qdc_qlong"]
        self.qdc_qshort = config["qdc_qshort"]
        self.qdc_gain = config["qdc_gain"]
        self.psd_gain = config["psd_gain"]
        self.trap_flat = config["trap_flat"]
        self.trap_gain = config["trap_gain"]
        self.trap_sampling = config["trap_sampling"]
        self.trap_shaping = config["trap_shaping"]
        self.trap_tau = config["trap_tau"]
        self.peak_pretrigger = config["peak_pretrigger"]
        self.peak_sampling = config["peak_sampling"]
        self.baseline_hold = config["baseline_hold"]
        self.baseline_len = config["baseline_len"]
        self.baseline_delay = config["baseline_delay"]
        self.baseline_mode = convert_to_enum(config["baseline_mode"], ConfigMCA.BaselineMode)
        self.pur_mode = convert_to_enum(config["pur_mode"], ConfigMCA.PurMode)
        self.pur_type = convert_to_enum(config["pur_paral"], ConfigMCA.PurType)
        self.pur_single_lenght = config["pur_len"]
        self.pur_double_lenght = config["pur_dlen"]
        self.risetime_mode = convert_to_enum(config["risetime_mode"], ConfigMCA.RisetimeMode)
        self.risetime_algorithm = convert_to_enum(config["risetime_sel"], ConfigMCA.RisetimeAlgorithm)
        self.risetime_pre = config["risetime_pre"]
        self.risetime_th1 = config["risetime_th1"]
        self.risetime_th2 = config["risetime_th2"]
        self.risetime_th3 = config["risetime_th3"]
        self.risetime_window = config["risetime_window"]


    def to_json(self):
        return {
            "trigger_mode": self.trigger_mode.value,
            "trigger_type": self.trigger_type.value,
            "trigger_edge": self.trigger_edge.value,
            "le_delta": self.le_delta,
            "le_inib": self.le_inib,
            "le_polarity": self.le_polarity.value,
            "le_threshold": self.le_threshold,
            "ft_flat": self.ft_flat,
            "ft_offset": self.ft_offset,
            "ft_polarity": self.ft_polarity.value,
            "ft_shaping": self.ft_shaping,
            "ft_tau": self.ft_tau,
            "ft_threshold": self.ft_threshold,
            "energy_mode": self.energy_mode.value,
            "qdc_post_inibit": self.qdc_post_inibit,
            "qdc_pre": self.qdc_pre,
            "qdc_qlong": self.qdc_qlong,
            "qdc_qshort": self.qdc_qshort,
            "qdc_gain": self.qdc_gain,
            "psd_gain": self.psd_gain,
            "trap_flat": self.trap_flat,
            "trap_gain": self.trap_gain, 
            "trap_sampling": self.trap_sampling,
            "trap_shaping": self.trap_shaping,
            "trap_tau": self.trap_tau,
            "peak_pretrigger": self.peak_pretrigger,
            "peak_sampling": self.peak_sampling,
            "baseline_hold": self.baseline_hold,
            "baseline_len": self.baseline_len,
            "baseline_delay": self.baseline_delay,
            "baseline_mode": self.baseline_mode.value,
            "pur_mode": self.pur_mode.value,
            "pur_type": self.pur_type.value,
            "pur_len": self.pur_single_lenght,
            "pur_dlen": self.pur_double_lenght,
            "risetime_mode": self.risetime_mode.value,
            "risetime_sel": self.risetime_algorithm.value,
            "risetime_pre": self.risetime_pre,
            "risetime_th1": self.risetime_th1,
            "risetime_th2": self.risetime_th2,
            "risetime_th3": self.risetime_th3,
            "risetime_window": self.risetime_window        
        }
        
    def __str__(self):
        properties = vars(self)
        return '\n'.join([f'{key}: {value}' for key, value in properties.items() if key.startswith('_')])
    
    @property
    def mca_mode(self):
        return self._mca_mode
    @mca_mode.setter
    def mca_mode(self, value):
        self._mca_mode = value

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
    def baseline_delay(self):
        return self._baseline_delay
    
    @baseline_delay.setter
    def baseline_delay(self, value):
        self._baseline_delay = value

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
    def peak_pretrigger(self):
        return self._peak_pretrigger
    
    @peak_pretrigger.setter
    def peak_pretrigger(self, value):
        self._peak_pretrigger = value
    
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
    def qdc_gain(self):
        return self._qdc_gain
    
    @qdc_gain.setter
    def qdc_gain(self, value):
        self._qdc_gain = value

    @property
    def psd_gain(self):
        return self._psd_gain
    
    @psd_gain.setter
    def psd_gain(self, value):
        self._psd_gain = value

    @property
    def risetime_pre(self):
        return self._risetime_pre
    
    @risetime_pre.setter
    def risetime_pre(self, value):
        self._risetime_pre = value
    
    @property
    def risetime_th1(self):
        return self._risetime_th1
    
    @risetime_th1.setter
    def risetime_th1(self, value):
        self._risetime_th1 = value
    
    @property
    def risetime_th2(self):
        return self._risetime_th2
    
    @risetime_th2.setter
    def risetime_th2(self, value):
        self._risetime_th2 = value

    @property
    def risetime_th3(self):
        return self._risetime_th3
    
    @risetime_th3.setter
    def risetime_th3(self, value):
        self._risetime_th3 = value

    @property
    def risetime_window(self):
        return self._risetime_window
    
    @risetime_window.setter
    def risetime_window(self, value):
        self._risetime_window = value

    @property
    def risetime_mode(self):
        return self._risetime_mode
    
    @risetime_mode.setter
    def risetime_mode(self, value):
        self._risetime_mode = value

    @property
    def risetime_algorithm(self):
        return self._risetime_algorithm
    
    @risetime_algorithm.setter
    def risetime_algorithm(self, value):
        self._risetime_algorithm = value

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
    def pur_single_lenght(self):
        return self._pur_single_lenght
    
    @pur_single_lenght.setter
    def pur_single_lenght(self, value):
        self._pur_single_lenght = value

    @property
    def pur_double_lenght(self):
        return self._pur_double_lenght
    
    @pur_double_lenght.setter
    def pur_double_lenght(self, value):
        self._pur_double_lenght = value

    @property
    def pur_mode(self):
        return self.pur_mode
    
    @pur_mode.setter
    def pur_mode(self, value):
        self._pur_mode = value

    @property
    def pur_type(self):
        return self._pur_type
    
    @pur_type.setter
    def pur_type(self, value):
        self._pur_type = value

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

    @property
    def trigger_edge(self):
        return self._trigger_edge
    
    @trigger_edge.setter
    def trigger_edge(self, value):
        self._trigger_edge = value

class ConfigAnalog:

    class Polarity(Enum):
        POSITIVE = "positive"
        NEGATIVE = "negative"

    class AnalogOut(Enum):
        TRIGGER_OUTPUT = "data_trigger_out"
        ENERGY_FILTER_OUTPUT = "energy_filter_output"
        BASELINE = "baseline"
        ENERGY_VALUE = "energy_value"
        RISETIME = "risetime"
        ANALOG_INPUT = "analog_input"

    def __init__(self):
        self.analog_in_polarity = ConfigAnalog.Polarity.POSITIVE
        self.analog_out = ConfigAnalog.AnalogOut.ENERGY_FILTER_OUTPUT
        self.analog_in_filter_enable = 0
        self.analog_in_filter_len = 0
        self.analog_in_delay = 0
        
    def __str__(self):
        properties = vars(self)
        return '\n'.join([f'{key}: {value}' for key, value in properties.items() if key.startswith('_')])
    
    def process_analog_json(self, config):
        self.analog_in_polarity = convert_to_enum(config["analog_in_polarity"], ConfigAnalog.Polarity)
        self.analog_out = convert_to_enum(config["analog_out"], ConfigAnalog.AnalogOut)
        self.analog_in_filter_enable = config["analog_in_filter_en"]
        self.analog_in_filter_len = config["analog_in_filter_len"]
        self.analog_in_delay =config["analog_in_delay"]
    
    def to_json(self):
        return {
            "analog_in_polarity": self.analog_in_polarity.value,
            "analog_out": self.analog_out.value,
            "analog_in_filter_en": self.analog_in_filter_enable,
            "analog_in_filter_len":self.analog_in_filter_len,
            "analog_in_delay":self.analog_in_delay
        }
    
    @property
    def analog_in_polarity(self):
        return self._analog_in_polarity

    @analog_in_polarity.setter
    def analog_in_polarity(self, value):
        self._analog_in_polarity = value

    @property
    def analog_out(self):
        return self._analog_out

    @analog_out.setter
    def analog_out(self, value):
        self._analog_out = value

    @property
    def analog_in_filter_enable(self):
        return self._analog_in_filter_enable

    @analog_in_filter_enable.setter
    def analog_in_filter_enable(self, value):
        self._analog_in_filter_enable = value

    @property
    def analog_in_filter_len(self):
        return self._analog_in_filter_len

    @analog_in_filter_len.setter
    def analog_in_filter_len(self, value):
        self._analog_in_filter_len = value

    @property
    def analog_in_delay(self):
        return self._analog_in_delay

    @analog_in_delay.setter
    def analog_in_delay(self, value):
        self._analog_in_delay = value
    

# Classe per la conversione e gestione dei valori
class ConfigDigitalIO:

    class Polarity(Enum):
        POSITIVE = "positive"
        NEGATIVE = "negative"

        # Assumo altri valori possibili qui, aggiungili secondo necessità

    class DigitalIn(Enum):
        EXTERNAL_TRIGGER = "external_trigger"
        EXTERNAL_ACQUISITION = "external_acquisition"
        EXTERNAL_RESET = "external_reset"
        EXTERNAL_T0 = "external_t0"

        # Assumo altri valori possibili qui, aggiungili secondo necessità

    class DigitalOut(Enum):
        TRIGGER = "trigger"
        ENERGY_VALID = "energy_valid"
        RISETIME_VALID = "risetime_valid"
        BASELINE_HOLD = "baseline_hold"
        ENERGY_GATE = "energy_gate"
        TOT = "time_over_threshold"
        PUR_VALID = "pur_valid"
        PUR_INIB = "pur_inib"
        PUR_REJ = "pur_rej"
        RESET = "reset"
        ACQUISITION = "acquisition"
        RUN = "run"
        T0 = "t0"

    def __init__(self):
        self.digital_in = ConfigDigitalIO.DigitalIn.EXTERNAL_TRIGGER
        self.digital_out = ConfigDigitalIO.DigitalOut.TRIGGER
        self.digital_out_delay = 0
        self.digital_out_width = 0
        self.digital_in_invert = 0
        self.t0_period = 1000000
        
    def __str__(self):
        properties = vars(self)
        return '\n'.join([f'{key}: {value}' for key, value in properties.items() if key.startswith('_')])
    
    def process_digital_json(self, config):
        self.digital_in = convert_to_enum(config["digital_in"], ConfigDigitalIO.DigitalIn)
        self.digital_out = convert_to_enum(config["digital_out"], ConfigDigitalIO.DigitalOut)
        self.digital_out_delay = config["digital_out_delay"]
        self.digital_out_width = config["digital_out_width"]
        self.digital_in_invert = config["digital_in_invert"]
        self.t0_period = config["t0_period"]
    
    def to_json(self):
        return {
            "digital_in": self.digital_in.value,
            "digital_out": self.digital_out.value,
            "digital_out_delay":self.digital_out_delay,
            "digital_out_width":self.digital_out_width,
            "digital_in_invert":self.digital_in_invert,
            "t0_period": self.t0_period
        }
    
    @property
    def digital_in(self):
        return self._digital_in

    @digital_in.setter
    def digital_in(self, value):
        self._digital_in = value

    @property
    def digital_out(self):
        return self._digital_out

    @digital_out.setter
    def digital_out(self, value):
        self._digital_out = value

    @property
    def digital_out_delay(self):
        return self._digital_out_delay

    @digital_out_delay.setter
    def digital_out_delay(self, value):
        self._digital_out_delay = value

    @property
    def digital_out_width(self):
        return self._digital_out_width

    @digital_out_width.setter
    def digital_out_width(self, value):
        self._digital_out_width = value

    @property
    def digital_out_invert(self):
        return self._digital_out_invert

    @digital_out_invert.setter
    def digital_out_invert(self, value):
        self._digital_out_invert = value

    @property
    def t0_period(self):
        return self._t0_period

    @t0_period.setter
    def t0_period(self, value):
        self._t0_period = value


class ConfigOscilloscope:
    class ScopeAnalog(Enum):
        TRAPEZOIDAL_BASELINE = "trapezoidal_baseline"
        SIGNAL_BASELINE = "signal_baseline"
        PEAK_STRETCHER_BASELINE = "peak_stretcher_baseline"
        DELTA_TRIGGER = "delta_trigger"
        TRAPEZOIDAL_TRIGGER = "trapezoidal_trigger"
        TRAPEZOIDAL = "trapezoidal"
        Q_LONG_VALUE = "q_long_value"
        Q_SHORT_VALUE = "q_short_value"
        PEAK_VALUE = "peak_value"
        BASELINE = "baseline"
        RISETIME = "risetime"

    class TriggerSource(Enum):
        FREE_RUNNING = "free_running"
        ANALOG_CHANNEL_1 = "analog_channel_1"
        ANALOG_CHANNEL_2 = "analog_channel_2"
        EXTERNAL_TRIGGER = "external_trigger"
        INTERNAL_TRIGGER = "internal_trigger"
        ENERGY_VALID = "energy_valid"
        REJECTED = "rejected"

    # class HISTROGRAM_SOURCE(Enum):
    #     ENERGY = "energy",
    #     RISETIME = "risetime",
    #     TIME = "risetime"
    
    # class PSD_SOURCE(Enum):
    #     ENERGY = "energy_",
    #     PSD = "psd",
    #     RISETIME = "risetime"


    def __init__(self):
        self.decimator = None
        self.pre_trigger = None
        self.scope_analog = None
        self.trigger_edge = None
        self.trigger_level = None
        self.trigger_source = None
        
    def __str__(self):
        properties = vars(self)
        return '\n'.join([f'{key}: {value}' for key, value in properties.items()])

    def process_scope_json(self, config):
        self.decimator = config["decimator"]
        self.pre_trigger = config["pre_trigger"]
        self.scope_analog = convert_to_enum(config["scope_analog"], ConfigOscilloscope.ScopeAnalog)
        self.trigger_edge = convert_to_enum(config["trigger_edge"], ConfigDigitalIO.Polarity)
        self.trigger_level = config["trigger_level"]
        self.trigger_source = convert_to_enum(config["trigger_source"], ConfigOscilloscope.TriggerSource)

    def to_json(self):
        return {
            "decimator": self.decimator,
            "pre_trigger": self.pre_trigger,
            "scope_analog": self.scope_analog.value,
            "trigger_edge": self.trigger_edge.value,
            "trigger_level": self.trigger_level,
            "trigger_source": self.trigger_source.value
        }
    
    @property
    def decimator(self):
        return self._decimator
    
    @decimator.setter
    def decimator(self, value):
        self._decimator = value
    
    @property
    def pre_trigger(self):
        return self._pre_trigger
    
    @pre_trigger.setter
    def pre_trigger(self, value):
        self._pre_trigger = value
    
    @property
    def scope_analog(self):
        return self._scope_analog
    
    @scope_analog.setter
    def scope_analog(self, value):
        self._scope_analog = value
    
    @property
    def trigger_edge(self):
        return self._trigger_edge
    
    @trigger_edge.setter
    def trigger_edge(self, value):
        self._trigger_edge = value
    
    @property
    def trigger_level(self):
        return self._trigger_level
    
    @trigger_level.setter
    def trigger_level(self, value):
        self._trigger_level = value
    
    @property
    def trigger_source(self):
        return self._trigger_source
    
    @trigger_source.setter
    def trigger_source(self, value):
        self._trigger_source = value

class StatisticsMCA:
    class DataItem:
        def __init__(self, name, value, min_value=None, max_value=None):
            self._name = name
            self._value = value
            self._min_value = min_value
            self._max_value = max_value
        
        @property
        def name(self):
            return self._name
        
        @property
        def value(self):
            return self._value
        
        @property
        def min_value(self):
            return self._min_value
        
        @property
        def max_value(self):
            return self._max_value

    def __init__(self):
        self._data = []
        self._result = None
        
        # Definizione manuale delle proprietà per gli elementi dei dati
        self.icr = self._get_data_item_by_name("ICR (Hz)")
        self.ocr = self._get_data_item_by_name("OCR (Hz)")
        self.input_count = self._get_data_item_by_name("INPUT COUNT")
        self.output_count = self._get_data_item_by_name("OUTPUT COUNT")
        self.lost_count = self._get_data_item_by_name("REJECTED COUNT")
        self.live_time_s = self._get_data_item_by_name("LIVE TIME (s)")

    def _get_data_item_by_name(self, name):
        for item in self._data:
            if item.name == name:
                return item
        return None

    def __str__(self):
        data_str = '\n'.join([f'{item.name}: {item.value}' for item in self._data])
        return f"Data:\n{data_str}\n"

    def process_json(self, json_data):
        for item in json_data["data"]:
            if "min_value" in item and "max_value" in item:
                data_item = self.DataItem(item["name"], item["value"], item["min_value"], item["max_value"])
            else:
                data_item = self.DataItem(item["name"], item["value"])
            self._data.append(data_item)
        self._result = json_data["result"]

        self.icr = self._get_data_item_by_name("ICR (cps)")
        self.ocr = self._get_data_item_by_name("OCR (cps)")
        self.input_count = self._get_data_item_by_name("INPUT COUNT")
        self.output_count = self._get_data_item_by_name("OUTPUT COUNT")
        self.lost_count = self._get_data_item_by_name("REJECTED COUNT")
        self.live_time_s = self._get_data_item_by_name("LIVE TIME (s)")        

    @property
    def result(self):
        return self._result
    

class ConfigAcquisition:

    class MCAMode(Enum):
        HARDWARE = "hardware"
        SOFTWARE = "software"

    # Definizione degli enum come specificato
    class AcquisitionMode(Enum):
        FREERUN = "freerun"
        COUNTS = "counts"
        TIME = "time_ms"

    class SpectrumType(Enum):
        RISETIME = "risetime"
        TIME = "time"
        INTERTIME = "intertime"
        ENERGY = "energy"
    
    class MultiparameterType(Enum):
        ENERGY_TIME = "energy_time"
        ENERGY_INTERTIME = "energy_intertime"
        ENERGY_RISETIME = "energy_risetime"
        ENERGY_PSD = "energy_psd"
    
    def __init__(self):
        self.mca_mode = ConfigAcquisition.MCAMode.SOFTWARE
        self.energy_cut_enable = False
        self.risetime_cut_enable = False
        self.psd_cut_enable = False
        self.risetime_min_cut = 0
        self.risetime_max_cut = 0
        self.energy_min_cut = 0
        self.energy_max_cut = 0
        self.psd_min_cut = 0
        self.psd_max_cut = 0
        self.energy_mode =  ConfigAcquisition.AcquisitionMode.FREERUN
        self.energy_target = 0
        self.time_mode =  ConfigAcquisition.AcquisitionMode.FREERUN
        self.time_target = 0
        self.multiparameter_mode = ConfigAcquisition.AcquisitionMode.FREERUN
        self.multiparameter_target = 0
        self.time_type = ConfigAcquisition.SpectrumType.TIME
        self.multiparameter_type = ConfigAcquisition.MultiparameterType.ENERGY_PSD  
        self.energy_dim = 16
        self.time_dim = 16
        self.multiparameter_dim = 10
        self.param1_dim = 16
        self.param2_dim = 16
        self.time_scale = 5
        self.multiparameter_scale = 5

    def process_acquisition_json(self, config):
        self.mca_mode =  convert_to_enum(config["mca_mode"],ConfigAcquisition.MCAMode) 
        self.energy_cut_enable = config["energy_cut_enable"]
        self.risetime_cut_enable = config["risetime_cut_enable"]
        self.psd_cut_enable = config["psd_cut_enable"]
        self.risetime_min_cut = config["risetime_min_cut"]
        self.risetime_max_cut = config["risetime_max_cut"]
        self.energy_min_cut = config["energy_min_cut"]
        self.energy_max_cut = config["energy_max_cut"]
        self.psd_min_cut = config["psd_min_cut"]
        self.psd_max_cut = config["psd_max_cut"]
        self.energy_mode =  convert_to_enum(config["energy_mode"],ConfigAcquisition.AcquisitionMode) 
        self.energy_target = config["energy_target"]
        self.time_mode =  convert_to_enum(config["time_mode"],ConfigAcquisition.AcquisitionMode) 
        self.time_target = config["time_target"]
        self.multiparameter_mode =  convert_to_enum(config["multiparameter_mode"],ConfigAcquisition.AcquisitionMode) 
        self.multiparameter_target = config["multiparameter_target"]
        self.time_type =  convert_to_enum(config["time_type"],ConfigAcquisition.SpectrumType) 
        self.multiparameter_type =  convert_to_enum(config["multiparameter_type"],ConfigAcquisition.MultiparameterType) 
        self.energy_dim = config["energy_dim"]
        self.time_dim = config["time_dim"]
        self.multiparameter_dim = config["multiparameter_dim"]
        self.param1_dim = config["param1_dim"]
        self.param2_dim = config["param2_dim"]
        self.time_scale = config["time_scale"]
        self.multiparameter_scale = config["multiparameter_scale"]
    
    def to_json(self):
        return {
            "mca_mode" : self.mca_mode.value,
            "energy_cut_enable": self.energy_cut_enable,
            "risetime_cut_enable": self.risetime_cut_enable,
            "psd_cut_enable": self.psd_cut_enable,
            "risetime_min_cut": self.risetime_min_cut,
            "risetime_max_cut": self.risetime_max_cut,
            "energy_min_cut": self.energy_min_cut,
            "energy_max_cut": self.energy_max_cut,
            "psd_min_cut": self.psd_min_cut,
            "psd_max_cut": self.psd_max_cut,
            "energy_mode": self.energy_mode.value,
            "energy_target": self.energy_target,
            "time_mode": self.time_mode.value,
            "time_target": self.time_target,
            "multiparameter_mode": self.multiparameter_mode.value,
            "multiparameter_target": self.multiparameter_target,
            "time_type": self.time_type.value,
            "multiparameter_type": self.multiparameter_type.value,
            "energy_dim": self.energy_dim,
            "time_dim": self.time_dim,
            "multiparameter_dim": self.multiparameter_dim,
            "param1_dim": self.param1_dim,
            "param2_dim": self.param2_dim,
            "time_scale": self.time_scale,
            "multiparameter_scale": self.multiparameter_scale
        }
        
    def __str__(self):
        properties = vars(self)
        return '\n'.join([f'{key}: {value}' for key, value in properties.items() if key.startswith('_')])
    
    @property
    def mca_mode(self):
        return self._mca_mode
    @mca_mode.setter
    def mca_mode(self, value):
        self._mca_mode = value

    @property
    def energy_cut_enable(self):
        return self._energy_cut_enable
    @energy_cut_enable.setter
    def energy_cut_enable(self, value):
        self._energy_cut_enable = value
        
    @property
    def risetime_cut_enable(self):
        return self._risetime_cut_enable
    @risetime_cut_enable.setter
    def risetime_cut_enable(self, value):
        self._risetime_cut_enable = value

    @property
    def risetime_min_cut(self):
        return self._risetime_min_cut
    @risetime_min_cut.setter
    def risetime_min_cut(self, value):
        self._risetime_min_cut = value

    @property
    def risetime_max_cut(self):
        return self._risetime_max_cut
    @risetime_max_cut.setter
    def risetime_max_cut(self, value):
        self._risetime_max_cut = value

    @property
    def energy_min_cut(self):
        return self._energy_min_cut
    @energy_min_cut.setter
    def energy_min_cut(self, value):
        self._energy_min_cut = value

    @property
    def energy_max_cut(self):
        return self._energy_max_cut
    @energy_max_cut.setter
    def energy_max_cut(self, value):
        self._energy_max_cut = value

    @property
    def psd_min_cut(self):
        return self._psd_min_cut
    @psd_min_cut.setter
    def psd_min_cut(self, value):
        self._psd_min_cut = value

    @property
    def psd_max_cut(self):
        return self._psd_max_cut
    @psd_max_cut.setter
    def psd_max_cut(self, value):
        self._psd_max_cut = value

    @property
    def energy_mode(self):
        return self._energy_mode
    @energy_mode.setter
    def energy_mode(self, value):
        self._energy_mode = value

    @property
    def energy_target(self):
        return self._energy_target
    @energy_target.setter
    def energy_target(self, value):
        self._energy_target = value

    @property
    def time_mode(self):
        return self._time_mode
    @time_mode.setter
    def time_mode(self, value):
        self._time_mode = value

    @property
    def time_target(self):
        return self._time_target
    @time_target.setter
    def time_target(self, value):
        self._time_target = value

    @property
    def multiparameter_mode(self):
        return self._multiparameter_mode
    @multiparameter_mode.setter
    def multiparameter_mode(self, value):
        self._multiparameter_mode = value

    @property
    def multiparameter_target(self):
        return self._multiparameter_target
    @multiparameter_target.setter
    def multiparameter_target(self, value):
        self._multiparameter_target = value

    @property
    def time_type(self):
        return self._time_type
    @time_type.setter
    def time_type(self, value):
        self._time_type = value

    @property
    def multiparameter_type(self):
        return self._multiparameter_type
    @multiparameter_type.setter
    def multiparameter_type(self, value):
        self._multiparameter_type = value

    @property
    def energy_dim(self):
        return self._energy_dim
    @energy_dim.setter
    def energy_dim(self, value):
        self._energy_dim = value

    @property
    def time_dim(self):
        return self._time_dim
    @time_dim.setter
    def time_dim(self, value):
        self._time_dim = value

    @property
    def multiparameter_dim(self):
        return self._multiparameter_dim
    @multiparameter_dim.setter
    def multiparameter_dim(self, value):
        self._multiparameter_dim = value

    @property
    def param1_dim(self):
        return self._param1_dim
    @param1_dim.setter
    def param1_dim(self, value):
        self._param1_dim = value

    @property
    def param2_dim(self):
        return self._param2_dim
    @param2_dim.setter
    def param2_dim(self, value):
        self._param2_dim = value

    @property
    def time_scale(self):
        return self._time_scale
    @time_scale.setter
    def time_scale(self, value):
        self._time_scale = value

    @property
    def multiparameter_scale(self):
        return self._multiparameter_scale
    @multiparameter_scale.setter
    def multiparameter_scale(self, value):
        self._multiparameter_scale = value

class OscilloscopeChannel:
    def __init__(self, analog, digital):
        self.analog = analog
        self.digital = digital

class OscilloscopeData:
    def __init__(self, wave):  
        self._channels = [] 

        for w in wave:
            analog = w["analog"][0]
            digitals = w["digital"]
            digital = [[int(value) for value in sub_array] for sub_array in digitals]

            channel = OscilloscopeChannel(analog, digital)
            self.channels.append(channel)
    
    @property
    def channels(self):
        return self._channels
    


class SmartMCA:
    url = ""  
    connected = False  
    cookie = None
    _API_PATH_ = "/mca/api"

    class Status(Enum):
        IDLE = "idle"
        RUNNING = "running"

    class ScaleMode (Enum):
        LINEAR = "linear"
        LOG = "log"

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
        config = ConfigMCA()
        config.process_config_json(j)
        return config
    
    def set_mca_configuration(self, config : ConfigMCA):
        j = config.to_json()
        r = self.http_post(self._API_PATH_ + "/HLL/hl_set_processing_param", j)
        if r["result"] != "ok":
            raise Exception(r["error"], 3)
    
    def get_digital_io_configuration(self):
        j = self.http_get(self._API_PATH_ + "/HLL/hl_get_digital_param")
        config = ConfigDigitalIO()
        config.process_digital_json(j)
        return config
    
    def set_digital_io_configuration(self, config : ConfigDigitalIO):
        j = config.to_json()
        r = self.http_post(self._API_PATH_ + "/HLL/hl_set_digital_param", j)
        if r["result"] != "ok":
            raise Exception(r["error"], 3)

    def get_analog_configuration(self):
        j = self.http_get(self._API_PATH_ + "/HLL/hl_get_analog_param")
        config = ConfigAnalog()
        config.process_analog_json(j)
        return config
    
    def set_digital_io_configuration(self, config : ConfigAnalog):
        j = config.to_json()
        r = self.http_post(self._API_PATH_ + "/HLL/hl_set_analog_param", j)
        if r["result"] != "ok":
            raise Exception(r["error"], 3)
    
    def get_acquisition_configuration(self):
        j = self.http_get(self._API_PATH_ + "/HLL/hl_get_acquisition_param")
        config = ConfigAcquisition()
        config.process_acquisition_json(j)
        return config
    
    def set_acquisition_configuration(self, config : ConfigAcquisition):
        j = config.to_json()
        r = self.http_post(self._API_PATH_ + "/HLL/hl_set_acquistion_param", j)
        if r["result"] != "ok":
            raise Exception(r["error"], 3)    
        
    def get_oscilloscope_configuration(self):
        j = self.http_get(self._API_PATH_ + "/HLL/hl_get_scope_param")
        config = ConfigOscilloscope()
        config.process_scope_json(j)
        return config
    
    def set_oscilloscope_configuration(self, config : ConfigOscilloscope):
        j = config.to_json()
        r = self.http_post(self._API_PATH_ + "/HLL/hl_set_scope_param", j)
        if r["result"] != "ok":
            raise Exception(r["error"], 3)

    def get_mca_statistics(self):
        j = self.http_get(self._API_PATH_ + "/HLL/hl_get_statistics")
        stats = StatisticsMCA()
        stats.process_json(j)
        return stats

    def reset_statistics(self):
        r = self.http_get(self._API_PATH_ + "/HLL/hl_reset_statistics")
        if r["result"] != "ok":
            raise Exception(r["error"], 3)
        
    def histogram_get_status(self):
        param = {
            "histo_type" : "energy"
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_get_status_histo", param)
        if j["result"] == "running":
            return SmartMCA.Status.RUNNING
        else:
            return SmartMCA.Status.IDLE
        
    def multiparametric_get_status(self):
        param = {
            "histo_type" : "energy_psd"
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_get_status_histo", param)
        if j["result"] == "running":
            return SmartMCA.Status.RUNNING
        else:
            return SmartMCA.Status.IDLE        
        
    def histogram_start(self, type:ConfigAcquisition.SpectrumType = ConfigAcquisition.SpectrumType.ENERGY):
        param = {
            "histo_type" : type.value
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_start_histo", param)

        
    def multiparametric_start(self, type:ConfigAcquisition.MultiparameterType = ConfigAcquisition.MultiparameterType.ENERGY_PSD):
        param = {
            "histo_type" : type.value
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_start_histo", param)
             
        
    def histogram_stop(self, type:ConfigAcquisition.SpectrumType = ConfigAcquisition.SpectrumType.ENERGY):
        param = {
            "histo_type" : type.value
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_stop_histo", param)

        
    def multiparametric_stop(self, type:ConfigAcquisition.MultiparameterType = ConfigAcquisition.MultiparameterType.ENERGY_PSD):
        param = {
            "histo_type" : type.value
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_stop_histo", param)
       
        
    def histogram_reset(self, type:ConfigAcquisition.SpectrumType = ConfigAcquisition.SpectrumType.ENERGY):
        param = {
            "histo_type" : type.value
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_reset_histo", param)
        
        
    def multiparametric_reset(self, type:ConfigAcquisition.MultiparameterType = ConfigAcquisition.MultiparameterType.ENERGY_PSD):
        param = {
            "histo_type" : type.value
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_reset_histo", param)

    def histogram_get(self, type:ConfigAcquisition.SpectrumType = ConfigAcquisition.SpectrumType.ENERGY, yscale:ScaleMode = ScaleMode.LINEAR, fit_data:bool=False, rebin:int=None):
        if yscale.value == "log":
            islog = True
        else:
            islog = False
            
        param = {
            "histo_type": type.value,
            "log": islog,
            "fit": fit_data
        }
        
        if rebin is not None:
            param["histo_rebin"] = rebin
        
        j = self.http_post(self._API_PATH_ + "/HLL/hl_get_histo", param)
        return j["data"], j["total_count"]
    
    def multiparametric_get(self, type:ConfigAcquisition.MultiparameterType = ConfigAcquisition.MultiparameterType.ENERGY_PSD, yscale:ScaleMode = ScaleMode.LINEAR, fit_data:bool=False, rebin:int=None):
        if yscale.value == "log":
            islog = True
        else:
            islog = False
            
        param = {
            "histo_type": type.value,
            "log": islog,
            "fit": fit_data
        }
        
        if rebin is not None:
            param["histo_rebin"] = rebin
        
        j = self.http_post(self._API_PATH_ + "/HLL/hl_get_histo", param)
        return j["data"], j["total_count"]
    

    def oscilloscope_get_data(self, enable_trace_signal : bool = True, enable_trace_processing : bool = True ):
        waves = []
        if enable_trace_signal:
            waves.append(0)
        if enable_trace_processing:
            waves.append(1)
        param = {
            "waves": waves,
        }
        j = self.http_post(self._API_PATH_ + "/HLL/hl_get_scope_data",param)
     
        return OscilloscopeData(j["wave"])
