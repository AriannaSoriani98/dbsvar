import os
import shutil

def div_dir(directoryIn,directoryOut1,directoryOut2,directoryOut3):
    # Assicurati che il percorso della directory sia corretto e accessibile
    if not os.path.exists(directoryIn):
        print(f"La directory {directoryIn} non esiste.")
        return

    # Crea le due nuove directory
    os.makedirs(directoryOut1, exist_ok=True)
    os.makedirs(directoryOut2, exist_ok=True)
    os.makedirs(directoryOut3, exist_ok=True)

    # Elenco dei file nella directory
    files = os.listdir(directoryIn)

    for file in files:
        if file.startswith(tuple('ABCDEFGHI')):
            # Sposta i file che iniziano con A-Y nella prima directory
            shutil.move(os.path.join(directoryIn, file), os.path.join(directoryOut1, file))
        elif file.startswith(tuple('JKLMNOPQR')):
            # Sposta i rimanenti file nella seconda directory
            shutil.move(os.path.join(directoryIn, file), os.path.join(directoryOut2, file))
        else: 
            # Sposta i rimanenti file nella seconda directory
            shutil.move(os.path.join(directoryIn, file), os.path.join(directoryOut3, file))

    print("Divisione completata.")

# Esempio di utilizzo
dir_train_input_imm= r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo\train\images'
dir_train_output_1_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_1\train\images'
dir_train_output_2_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_2\train\images'
dir_train_output_3_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_3\train\images'
div_dir(dir_train_input_imm,dir_train_output_1_imm,dir_train_output_2_imm,dir_train_output_3_imm)

dir_train_input_label= r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo\train\labels'
dir_train_output_1_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_1\train\labels'
dir_train_output_2_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_2\train\labels'
dir_train_output_3_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_3\train\labels'
div_dir(dir_train_input_label,dir_train_output_1_label,dir_train_output_2_label,dir_train_output_3_label)

dir_val_input_imm= r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo\valid\images'
dir_val_output_1_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_1\valid\images'
dir_val_output_2_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_2\valid\images'
dir_val_output_3_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_3\valid\images'
div_dir(dir_val_input_imm,dir_val_output_1_imm,dir_val_output_2_imm,dir_val_output_3_imm)

dir_val_input_label= r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo\valid\labels'
dir_val_output_1_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_1\valid\labels'
dir_val_output_2_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_2\valid\labels'
dir_val_output_3_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_3\valid\labels'
div_dir(dir_val_input_label,dir_val_output_1_label,dir_val_output_2_label,dir_val_output_3_label)

dir_test_input_imm= r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo\test\images'
dir_test_output_1_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_1\test\images'
dir_test_output_2_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_2\test\images'
dir_test_output_3_imm = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_3\test\images'
div_dir(dir_test_input_imm,dir_test_output_1_imm,dir_test_output_2_imm,dir_test_output_3_imm)

dir_test_input_label= r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo\test\labels'
dir_test_output_1_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_1\test\labels'
dir_test_output_2_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_2\test\labels'
dir_test_output_3_label = r'C:\Users\Arianna\Documents\Magistrale\Visione Artificiale e Riconoscimento\dbsvar\asl_yolo_3\test\labels'
div_dir(dir_test_input_label,dir_test_output_1_label,dir_test_output_2_label,dir_test_output_3_label)