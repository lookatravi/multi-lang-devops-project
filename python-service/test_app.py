    steps:
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          cd python-service
          python -m pip install --upgrade pip
          pip install -r requirements.txt  # Install all dependencies
          pip install pytest  # Install pytest for running tests

      - name: Run Python tests
        run: |
          cd python-service
          pytest test_app.py  # Run the specific test file

      - name: List files in python-service
        run: |
          cd python-service
          ls -al  # Verify that test_app.py exists
