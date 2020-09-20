
from .arg_parser import get_parser
from .raw_data_class import MidiMidiDataset, XmlMidiDataset
from .feature_extraction import MidiMidiFeatureExtractor, XmlMidiFeatureExtractor
from .constant import MIDI_MIDI_FEATURE_LIST, XML_MIDI_FEATURE_LIST
from . import utils

def generate():
    p = get_parser()
    args = p.parse_args()

    emotion_path = args.path.joinpath("total")
    emotion_save_path = args.path.joinpath("save")
    
    # make dataset
    if args.direct:
        # midi - midi direct matching
        dataset = MidiMidiDataset(emotion_path, split=5)
        utils.save_datafile(emotion_save_path,'5sec_split_dataset.dat', dataset)
        dataset = utils.load_datafile(emotion_save_path, '5sec_split_dataset.dat')
        # extract features
        extractor = MidiMidiFeatureExtractor(dataset.set_list, MIDI_MIDI_FEATURE_LIST)
    else:
        # score - midi matching
        dataset = XmlMidiDataset(emotion_path)
        utils.save_datafile(emotion_save_path, 'xml_midi_matched.dat', dataset)
        dataset = utils.load_datafile(emotion_save_path, 'xml_midi_matched.dat')
        # extract features
        extractor = XmlMidiFeatureExtractor(dataset.set_list, XML_MIDI_FEATURE_LIST, split=16)
    
    feature_data = extractor.extract_features()
    
    utils.save_datafile(emotion_save_path, args.save_name, feature_data)



if __name__ == "__main__":
    generate()
