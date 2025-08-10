from customer_analytics.ingestion import read_data_in_chunks
from customer_analytics.cleaning import clean_chunk
from customer_analytics.transformation import compute_aggregates, z_score_filter
from customer_analytics.utils import validate_country_codes, concat_subsets
from customer_analytics.analysis import generate_profile, log_basic_summary

def main():
    all_cleaned = []
    for chunk in read_data_in_chunks():
        cleaned = clean_chunk(chunk)
        filtered = z_score_filter(cleaned)
        validated = validate_country_codes(filtered)
        all_cleaned.append(validated)
    
    full_df = concat_subsets(all_cleaned)
    log_basic_summary(full_df)
    aggregates = compute_aggregates(full_df)
    print(aggregates.head())
    generate_profile(full_df)

if __name__ == "__main__":
    main()
