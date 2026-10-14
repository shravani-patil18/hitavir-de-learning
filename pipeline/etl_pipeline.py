"""
ETL Pipeline - Hitavir Tech
Extract, Transform, Load
"""

class ETLPipeline:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.data = None

    def extract(self):
        print(f"Extracting data from {self.source}...")
        self.data = {
            "records": 1000,
            "source": self.source
        }
        return self

    def transform(self):
        print("Transforming and cleaning data...")
        self.data["status"] = "cleaned"
        self.data["records_after"] = 950
        return self

    def load(self):
        print(f"Loading data to {self.destination}...")
        print(f"Pipeline complete: {self.data}")
        return self

    def run(self):
        return self.extract().transform().load()


if __name__ == "__main__":
    pipeline = ETLPipeline(
        source="postgres://db.hitavir.tech/raw",
        destination="s3://hitavir-warehouse/processed"
    )
    pipeline.run()
