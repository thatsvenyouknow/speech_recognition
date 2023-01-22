import Levenshtein 
import librosa

def rtf(model_time, file_path):
    """
    Real-Time Factor:
    - model_time: time taken by the system to process input
    - file_path: path to audio file (.wav)
    """
    audio_dur = librosa.get_duration(filename=file_path)
    return model_time/audio_dur

def wer(ground_truth, model_out):
    """
    Word Error Rate:
    - input
        - ground_truth: ground truth [str or list]
        - model_out: model output [str or list]
    - vars_created
        - n_sub: number of substitutions in output text compared to ground truth
        - n_del: number of deletions performed
        - n_insert: number of insertions performed
        - n_corr: number of correct words
    """
    if isinstance(ground_truth, str):
        ground_truth = [ground_truth]

    if isinstance(model_out, str):
        model_out = [model_out]

    if len(model_out) == 0:
        raise ValueError("model output is empty")

    if model_out[0].lower().strip() == ground_truth[0]:
        return 1.0

    else: #if ground_truth != model output
        n_sub, n_del, n_insert, n_corr = 0, 0, 0, 0

        for input, output in zip(ground_truth, model_out):
            output = output.lower().strip() #lower and remove trailing spaces
            output = output.replace(".", "").replace(",", "") #remove punctuation
            editops = Levenshtein.editops(input, output)
            n_sub_trial = sum(1 if op[0] == "replace" else 0 for op in editops)
            n_del_trial = sum(1 if op[0] == "delete" else 0 for op in editops)
            n_sub += n_sub_trial
            n_del += n_del_trial
            n_insert += sum(1 if op[0] == "insert" else 0 for op in editops)
            n_corr += len(input.split()) - (n_sub_trial + n_del_trial)
        
        return float(n_sub + n_del + n_insert)/float(n_sub + n_del + n_corr)





    
