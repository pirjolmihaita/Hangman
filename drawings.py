def hangman(i):
    hangman_drawings = (
                     '''
                                   ______
                                  |      |        
                                         |      
                                         |     
                                         |         
                                         |     
                                _________|__
                     ''',
                     '''
                                   ______
                                  |      |        
                                  O      |      
                                         |     
                                         |         
                                         |     
                                _________|__
                     ''',
                     '''
                                   ______
                                  |      |        
                                  O      |      
                                  |      |     
                                         |         
                                         |     
                                _________|__
                     ''',
                     '''
                                   ______
                                  |      |        
                                  O      |      
                                 /|      |     
                                         |         
                                         |     
                                _________|__
                     ''',
                     '''
                                   ______
                                  |      |        
                                  O      |      
                                 /|\     |     
                                         |         
                                         |     
                                _________|__
                    ''',
                    '''
                                   ______
                                  |      |        
                                  O      |      
                                 /|\     |     
                                  |      |         
                                         |     
                                _________|__
                    ''',
                    '''
                                   ______
                                  |      |        
                                  O      |      
                                 /|\     |     
                                  |      |         
                                 /       |     
                                _________|__
                    ''',
                    '''
                                   ______
                                  |      |        
                                  O      |      
                                 /|\     |     
                                  |      |         
                                 / \     |     
                                _________|__
                    ''')
    return hangman_drawings[i]




