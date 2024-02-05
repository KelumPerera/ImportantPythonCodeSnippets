
# Important Polars Codes


import polars as pl    # Version 0.20.3
import pyarrow as pa   # Version 11.0.0
import pyarrow.parquet as pq


pl_df = pl.DataFrame({
                          "Name": ["ABC","DEF","GHI",'JKL'],
                          "date": ["2024-01-01","2024-01-10","2023-01-29","2023-01-29"],
                          "price":[1000,1500,1800,2100] ,
                          })

pl_df = pl_df.with_columns(date= pl.col("date").cast(pl.Date))

# write Polars dataframe to disk as parquet dataset    
pq.write_to_dataset( pl_df.to_arrow(), root_path=r"C:\Users\Kelum desktop PC\Downloads\test_pl", partition_cols=["date"],
                        compression ='gzip',existing_data_behavior='overwrite_or_ignore')
                        
# Have a schema object of data written to parquet dataset
pd_df_schema = pa.Schema.from_pandas(pl_df.to_pandas())

# Read data written to parquet dataset
pq_df = pq.read_table(r"C:\Users\Kelum desktop PC\Downloads\test_pl",
                      schema=pd_df_schema,
                      )

# I want to use this parquest object to create a agreegate result via Polars

df = (pl.from_pandas(pq_df.to_pandas()).lazy()
      .group_by(["date"])
      .agg(
          [
              pl.col("price").sum().alias("grouped_sum"),
              pl.col("price").count().alias("grouped_count"),])
      ).collect(streaming=True)
