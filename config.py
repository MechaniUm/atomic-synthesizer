query = '''SELECT Symbol, ElementName, IsotopeName, Description, Usage, ParentID, ID
    FROM atom
    WHERE P=:count_p AND
    N=:count_n'''

error_query = '''select N from atom where P=:count_p'''

folder_path = '/home/pi/Documents/synthesizer/'
