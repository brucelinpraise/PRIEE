from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample database of schemes
SCHEMES = [
    {
        'id': 1,
        'name': 'Pradhan Mantri Jan Dhan Yojana',
        'description': 'Financial inclusion to ensure access to financial services.',
        'eligibility': 'All Indian citizens.',
        'benefits': 'Bank accounts, insurance, pension.',
        'link': 'https://pmjdy.gov.in'
    },
    {
        'id': 2,
        'name': 'Pradhan Mantri Awas Yojana',
        'description': 'Affordable housing for urban poor.',
        'eligibility': 'Economically weaker sections, low and middle-income groups.',
        'benefits': 'Subsidy on home loan interest rates.',
        'link': 'https://pmaymis.gov.in'
    },
    {
        'id': 3,
        'name': 'Pradhan Mantri Mudra Yojana',
        'description': 'Provides loans up to 10 lakhs to non-corporate, non-farm small/micro enterprises.',
        'eligibility': 'Non-corporate small business segment.',
        'benefits': 'Loans up to 10 lakhs under Shishu, Kishor, and Tarun categories.',
        'link': 'https://www.mudra.org.in'
    },
    {
        'id': 4,
        'name': 'Pradhan Mantri Jeevan Jyoti Bima Yojana',
        'description': 'Life insurance scheme for people aged 18 to 50 years.',
        'eligibility': 'Aged between 18 and 50 years with a bank account.',
        'benefits': 'Life insurance cover of 2 lakhs at a premium of 330 per annum.',
        'link': 'https://www.jansuraksha.gov.in/Files/PMJJBY/English/PMJJBY.pdf'
    },
    {
        'id': 5,
        'name': 'what is pension scheme',
        'description': 'Pension scheme for unorganized sector workers.',
        'eligibility': 'Indian citizens aged between 18 and 40 years.',
        'benefits': 'Monthly pension between 1000 to 5000 after the age of 60.',
        'link': 'https://www.npscra.nsdl.co.in/scheme-details.php'
    },
    {
        'id': 6,
        'name': 'Pradhan Mantri Kaushal Vikas Yojana (PMKVY)',
        'description': 'Skill development training aimed to increase employability.',
        'eligibility': 'Unemployed youth, school/college dropouts, low-income groups.',
        'benefits': 'Skill training and certification.',
        'link': 'https://pmkvyofficial.org'
    },
    {
        'id': 7,
        'name': 'Pradhan Mantri Fasal Bima Yojana (PMFBY)',
        'description': 'Crop insurance scheme to provide insurance coverage and financial support to farmers in case of crop failure.',
        'eligibility': 'Farmers owning land and cultivating crops.',
        'benefits': 'Financial support in case of crop damage due to natural calamities.',
        'link': 'https://pmfby.gov.in'
    },
    {
        'id': 8,
        'name': 'Pradhan Mantri Suraksha Bima Yojana (PMSBY)',
        'description': 'Accident insurance scheme for individuals.',
        'eligibility': 'Indian citizens aged between 18 and 70 years.',
        'benefits': 'Accidental death and disability cover.',
        'link': 'https://www.jansuraksha.gov.in/Forms-PMSBY.aspx'
    },
    {
        'id': 9,
        'name': 'Pradhan Mantri Krishi Sinchai Yojana (PMKSY)',
        'description': 'Irrigation scheme to ensure water availability for every farm field.',
        'eligibility': 'Farmers, agricultural landowners.',
        'benefits': 'Improved water use efficiency, increased crop yield.',
        'link': 'https://pmksy.gov.in'
    },
    {
        'id': 10,
        'name': 'Pradhan Mantri Gramin Awaas Yojana (PMGAY)',
        'description': 'Housing scheme for rural areas.',
        'eligibility': 'BPL families, people living in kutcha houses.',
        'benefits': 'Financial assistance for the construction of houses.',
        'link': 'https://pmayg.nic.in'
    },
    {
        'id': 11,
        'name': 'Pradhan Mantri Gram Sadak Yojana (PMGSY)',
        'description': 'Rural road connectivity scheme.',
        'eligibility': 'Rural habitations, unconnected by all-weather roads.',
        'benefits': 'All-weather road connectivity to eligible rural habitations.',
        'link': 'https://pmgsy.nic.in'
    },
    {
        'id': 12,
        'name': 'Pradhan Mantri Matru Vandana Yojana (PMMVY)',
        'description': 'Maternity benefit program for pregnant and lactating women.',
        'eligibility': 'Pregnant and lactating women aged 19 and above.',
        'benefits': 'Cash incentives for the first living child.',
        'link': 'https://pmmvy.gov.in'
    },
    {
        'id': 13,
        'name': 'Sukanya Samriddhi Yojana (SSY)',
        'description': 'Saving scheme for the girl child.',
        'eligibility': 'Parents/guardians of a girl child aged 10 years or less.',
        'benefits': 'Tax benefits, high interest rate.',
        'link': 'https://www.nsiindia.gov.in/sukanya-samriddhi-account'
    },
    {
        'id': 14,
        'name': 'National Rural Employment Guarantee Scheme (MGNREGA)',
        'description': 'Guaranteed wage employment for rural households.',
        'eligibility': 'Adult members of rural households willing to do unskilled manual work.',
        'benefits': 'Guaranteed 100 days of wage employment in a financial year.',
        'link': 'https://nrega.nic.in/netnrega/home.aspx'
    },
    {
        'id': 15,
        'name': 'Ayushman Bharat Pradhan Mantri Jan Arogya Yojana (AB-PMJAY)',
        'description': 'Health insurance scheme for poor and vulnerable families.',
        'eligibility': 'Families identified as deprived and vulnerable based on Socio-Economic Caste Census (SECC) data.',
        'benefits': 'Cashless treatment at empaneled hospitals, coverage up to 5 lakhs per family per year.',
        'link': 'https://pmjay.gov.in'
    }
]

def get_all_schemes():
    return SCHEMES

def get_scheme_by_id(scheme_id):
    for scheme in SCHEMES:
        if scheme['id'] == scheme_id:
            return scheme
    return None

@app.route('/schemes', methods=['GET'])
def fetch_schemes():
    schemes = get_all_schemes()
    return jsonify(schemes)

@app.route('/scheme/<int:scheme_id>', methods=['GET'])
def fetch_scheme(scheme_id):
    scheme = get_scheme_by_id(scheme_id)
    if scheme:
        return jsonify(scheme)
    else:
        return jsonify({'error': 'Scheme not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

