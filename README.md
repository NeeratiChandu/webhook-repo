1.Run the Flask Application:

   Start your Flask application by running:
      python app.py
      
2.Set Up a Virtual Environment:
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies:

3.Install Flask and PyMongo:
pip install Flask pymongo

- Receives webhook events for:
  - Push actions
  - Pull request submissions
  - Merges
- Stores event data in MongoDB
- Provides a UI to display the latest events

## Setup Instructions

1. **Create a New Repository**:
   - Create a new GitHub repository named `webhook-repo`.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/webhook-repo.git
   cd webhook-repo
