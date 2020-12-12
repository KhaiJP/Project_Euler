#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image


# In[2]:


def assist(num):
    return num*31//255


# In[3]:


def get16citColour(tp):
    return ((assist(tp[2])) << 11 | (assist(tp[1])) << 6 | (assist(tp[0]) <<1))%(2**17)


# In[13]:


def array_generator(tp, header_name='./colour_info.h', variable_name='colour_info',save_C_array=True):
    '''
    tp is the tuple of the image files to be shown in the LED matrix with size 64x32.
    the elements of tp must be str.
    
    header_name is the name of the header file to be created.
    default is 'colour_info.h' stored in the current directory.
    
    variable_name is the name of the array to be created.
    default is 'colour_info'.
    '''
    
#   check if all the variables have proper type.
    if type(tp) != tuple: return print('1st variable, tp, must be tuple.')
    if type(header_name) != str: return print('2nd variable, header_name, must be string.')
    if type(variable_name) != str: return print('3rd variable, variable_name, must be string.')
    
    
    if header_name[-2:]!='.h': header_name+='.h'
    
    x_length=64 # number of pixels of the matrix along the horizontal direction
    y_length=32 # number of pixels of the matrix along the vertical direction
    images=[Image.open(j).resize((x_length,y_length)) for j in tp]
    number_of_pics=len(tp)
    
    f=lambda n,x,y,:images[n].getpixel((x,y))
    
    
    Colour=[[[] for j in range(x_length)] for k in range(number_of_pics)]
    colour_info="uint16_t " + variable_name + "[" + str(x_length*number_of_pics) + "][" + str(y_length) +"]={"
    for n in range(number_of_pics):
        colour_info+='{'
        for x in range(x_length):
            colour_info+='{'
            for y in range(y_length):
                Colour[n][x].append(get16citColour(f(n,x,y)))
                colour_info+=str(Colour[n][x][y])+','
            colour_info=colour_info[:-1]+'},'
        colour_info=colour_info[:-1]+'},'
    colour_info=colour_info[:-1]+'};'
    
    if save_C_array:
        header=open(header_name,mode='w',encoding='UTF-8')
        header.write(colour_info)
        header.close()
    
    return Colour


# In[18]:


def print_new_Image(Image_tuple,header_name='./colour_info.h',save_new_pic=False,pic_name='created_by_print_new_Image',extension='png',x_length=0,y_length=32):
    a=array_generator(Image_tuple,save_C_array=False)
    if x_length==0:
        for j in range(len(Image_tuple)):
            length+=Image_tuple[j].size[0]
    img=Image.new('RGB', (Image_tuple,32),65355)
    for n in range(len(a)):
        for x in range(len(a[n])):
            for y in range(len(a[n][x])):
                img.putpixel((n*64+x,y),((a[n][x][y]>>1)%(2**5)*255//31,(a[n][x][y]>>6)%(2**5)*255//31,(a[n][x][y]>>11)*255//31))
    img.show()
    if save_new_Image: img.save(pic_name+extension)
    return img


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


a


# In[ ]:




