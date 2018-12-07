mysql -u root -p <DBProject.sql

width=`identify -format %w ~/websites/DBProject/src/MemeGenerator/static/MemeGenerator/sociallyAwkwardPenguin.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"Hey, what's up?"  ~/websites/DBProject/src/MemeGenerator/static/MemeGenerator/sociallyAwkwardPenguin.jpg +swap -gravity north -composite ~/websites/DBProject/src/MemeGenerator/media/MemeGenerator/temp.jpg
width=`identify -format %w ~/websites/DBProject/src/MemeGenerator/static/MemeGenerator/sociallyAwkwardPenguin.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"Good, you?"  ~/websites/DBProject/src/MemeGenerator/media/MemeGenerator/temp.jpg +swap -gravity south -composite ~/websites/DBProject/src/MemeGenerator/media/MemeGenerator/admin1.jpg


width=`identify -format %w ~/websites/DBProject/src/MemeGenerator/static/MemeGenerator/rickAstley.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"Never Gonna Give You Up"  ~/websites/DBProject/src/MemeGenerator/static/MemeGenerator/rickAstley.jpg +swap -gravity north -composite ~/websites/DBProject/src/MemeGenerator/media/MemeGenerator/admin2.jpg


echo "Setup Complete"