def fit(model, images, labels, epochs, batch_size=128):     
    for epoch_counter in range(epochs):         print(f"Epoch 
{epoch_counter}")         batch_generator = BatchGener- 
ator(images, labels)         for batch_counter in range(batch_gener- 
ator.num_batches):             images_batch, labels_batch = batch_- 
generator.next()             loss = one_training_step(model, images_- 
batch, labels_batch)             if batch_counter % 100 == 0:           
      print(f"loss at batch {batch_counter}: {loss:.2f}") 
 