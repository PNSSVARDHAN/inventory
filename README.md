<h1>Inventory Management System</h1>

<p><strong>Project Overview:</strong> <br>
The <strong>Inventory Management System</strong> is a web-based application designed to help businesses efficiently track, manage, and organize their inventory. It allows users to add, update, and monitor stock levels, ensuring better control over supply chain operations.
</p>

<h2>Features</h2>
<ul>
  <li><strong>Product Management</strong> – Add, update, and remove products with details like name, category, quantity, and price.</li>
  <li><strong>Stock Tracking</strong> – Monitor available stock, receive low-stock alerts, and manage inventory levels efficiently.</li>
  <li><strong>Supplier Management</strong> – Keep track of suppliers, their products, and order history.</li>
  <li><strong>Role-Based Access</strong> – Admins manage inventory, while staff can view stock and update quantities.</li>
  <li><strong>Data Storage</strong> – Uses <strong>SQLite3</strong> for efficient inventory record management.</li>
</ul>

<h2>Technology Stack</h2>
<ul>
  <li><strong>Frontend:</strong> HTML, CSS</li>
  <li><strong>Backend:</strong> Django (Python)</li>
  <li><strong>Database:</strong> SQLite3</li>
</ul>

<h2>Installation Guide</h2>
<ol>
  <li><strong>Clone the Repository:</strong> 
    <pre><code>git clone https://github.com/PNSSVARDHAN/Inventory-Management-System.git
cd Inventory-Management-System</code></pre>
  </li>
  <li><strong>Set Up a Virtual Environment (Optional but Recommended):</strong> 
    <pre><code>python -m venv env  
source env/bin/activate  # On Windows: env\Scripts\activate</code></pre>
  </li>
  <li><strong>Install Dependencies:</strong> 
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li><strong>Run Migrations:</strong> 
    <pre><code>python manage.py migrate</code></pre>
  </li>
  <li><strong>Start the Development Server:</strong> 
    <pre><code>python manage.py runserver</code></pre>
  </li>
</ol>

<p>Access the system at <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a></p>

<h2>Usage Instructions</h2>
<ul>
  <li><strong>Admin Dashboard:</strong> Add or update products, view stock levels, and manage suppliers.</li>
  <li><strong>Stock Overview:</strong> Monitor available stock and get alerts for low inventory.</li>
</ul>

<h2>Future Enhancements</h2>
<ul>
  <li>Integration with Barcode Scanners</li>
  <li>Automated Purchase Order Generation</li>
  <li>Advanced Analytics for Inventory Trends</li>
</ul>

<h2>Contributing</h2>
<p>If you’d like to contribute, feel free to fork the repository and submit a pull request.</p>

<h2>License</h2>
<p>This project is open-source under the <strong>MIT License</strong>.</p>
