import re
import helper

# Sample public reports as a single string
reports = "Critical water shortage in our town demands immediate attention. Ministry of Environment, we need assistance night safety street"

# Define ministry agencies and their associated keywords
ministries = {
    "Kementerian Pendidikan, Kebudayaan, Riset dan Teknologi": helper.generate_keyword("kementerianPendidikan.txt"),
    "Kementerian Komunikasi dan Informatika": helper.generate_keyword("kementerianKomunikasi.txt"),
    "Kementerian Sosial": helper.generate_keyword("kementerianSosial.txt"),
    "Kepolisian Negara Republik Indonesia": helper.generate_keyword("kepolisianNegara.txt"),
    "Kementerian Kelautan dan Perikanan": helper.generate_keyword("kementerianKelautan.txt"),
    "Badan Kepegawaian Negara": helper.generate_keyword("kepegawaianNegara.txt"),
    "Kementerian Dalam Negeri": helper.generate_keyword("kementerianDalamNegeri.txt"),
    "Kementerian Pekerjaan Umum dan Perumahan Rakyat": helper.generate_keyword("kementerianPekerjaan.txt"),
    "Kementrian Agama": helper.generate_keyword("kementerianAgama.txt"),
    "Otoritas Jasa Keuangan": helper.generate_keyword("otoritasJasaKeuangan.txt"),
}

# Function to filter reports to ministries based on keywords and count the matches
def filter_reports(report):
    filtered_reports = {ministry: {"keyword_count": 0} for ministry in ministries}

    report = report.lower()  # Convert report to lowercase for case-insensitive matching

    for ministry, keywords in ministries.items():
        keyword_count = 0
        for keyword in keywords:
            matches = re.findall(rf"\b{re.escape(keyword)}\b", report)
            keyword_count += len(matches)

        filtered_reports[ministry]["keyword_count"] = keyword_count

    # Find the ministry with the highest keyword count
    max_keyword_count = max(filtered_reports.values(), key=lambda x: x["keyword_count"])["keyword_count"]

    # Print only the ministries with the highest keyword count
    for ministry, data in filtered_reports.items():
        if data["keyword_count"] == max_keyword_count:
            return ministry

# Filter the reports and count the keywords
# filtered_reports = filter_reports(reports, ministries)

