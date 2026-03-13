# Crack the Codebase - Pipeline Entry
import data_cleaner
import fairness_metrics
import report_generator
SOURCE_FILE = "cvr-crack-the-codebase\dataset.csv"

def execute_pipeline():
    print("Initializing Applicant Pipeline...")
    
    raw = data_cleaner.loader_func(SOURCE_FILE)
    
    print("Scrubbing messy data...")
    cleaned = data_cleaner.func_alpha_9(raw)
    
    print("Calculating demographic parity...")
    final_metrics = fairness_metrics.engine_run(cleaned)
    
    print("Generating HR Report...")
    report_generator.write_output(final_metrics)
    
    print("Pipeline Execution Complete!")

if __name__ == "__main__":
    execute_pipeline()
